import opencor as oc
import numpy as np
import os
import xml.etree.ElementTree as ET
from importlib import import_module  # Only used for debugging


class SimulationHelper():
    def __init__(self, cellml_path, dt,
                 sim_time, solver_info=None,
                 pre_time=0.0):

        # TODO comment this out
        # self.resource_module = import_module('psutil')

        self.cellml_path = cellml_path  # path to cellml file
        self.dt = dt  # time step
        self.stop_time = pre_time + sim_time  # full time of simulation
        self.pre_steps = int(pre_time / dt)  # number of steps to do before storing data (used to reach steady state)
        self.n_steps = int(sim_time / dt)  # number of steps for storing data
        self.simulation = oc.open_simulation(cellml_path)
        if not self.simulation.valid():
            raise RuntimeError(f'simulation object opened from {cellml_path} is not valid')

        self.data = self.simulation.data()
        if solver_info is None:
            solver_info = {'MaximumNumberOfSteps': 5000, 'MaximumStep': 0.0001}

        valid_solver_keys = [key for key in self.data.odeSolverProperties()]
        for key, value in solver_info.items():
            if key not in valid_solver_keys:
                raise KeyError(
                    f"{key} is not a valid key for the solver properties in CVODE. "
                    f"Valid keys are: {valid_solver_keys}"
                )
            self.data.set_ode_solver_property(key, value)

        self.data.set_point_interval(self.dt)  # time interval for data storage
        self.data.set_starting_point(0)
        self.data.set_ending_point(self.stop_time)
        self.tSim = np.linspace(pre_time, self.stop_time, self.n_steps + 1)  # time values for stored part of simulation

    # inner psutil function # TODO only needed for memory checking
    def process_memory(self):
        process = self.resource_module.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss

    def run(self):
        try:
            self.simulation.run()
        except RuntimeError:
            print("Failed to converge")
            print('restarting simulation object')
            self.simulation.reset()
            self.simulation.release_all_values()
            self.simulation.clear_results()
            return False

        return True

    def reset_and_clear(self, only_one_exp=-1):
        self.simulation.reset(True)
        self.simulation.release_all_values()
        self.simulation.clear_results()

    def reset_states(self):
        self.simulation.reset(False)  # True resets everything, False resets only the states

    # --- minimal helper additions ---
    def list_states(self):
        return [name for name in self.simulation.results().states()]

    def list_algebraics(self):
        return [name for name in self.simulation.results().algebraic()]

    def list_constants(self):
        return [name for name in self.data.constants()]

    def list_all_variables(self):
        return self.list_states() + self.list_algebraics() + self.list_constants()

    def list_all_parameters(self):
        return [name for name in self.data.states()] + [name for name in self.data.constants()]

    def get_time_unit(self):
        """Read the time unit from the CellML XML, avoiding older OpenCOR API calls like voi()."""
        try:
            tree = ET.parse(self.cellml_path)
            root = tree.getroot()
            for elem in root.iter():
                tag = elem.tag.split('}', 1)[-1]
                if tag == 'component' and elem.attrib.get('name') == 'environment':
                    for child in elem:
                        child_tag = child.tag.split('}', 1)[-1]
                        if child_tag == 'variable' and child.attrib.get('name') == 'time':
                            return child.attrib.get('units', '')
        except Exception:
            pass
        return ''

    def get_variable_unit(self, variable_name):
        if variable_name == 'time':
            return self.get_time_unit()
        try:
            if variable_name in self.simulation.results().states():
                obj = self.simulation.results().states()[variable_name]
                return obj.unit() if hasattr(obj, 'unit') else ''
            if variable_name in self.simulation.results().algebraic():
                obj = self.simulation.results().algebraic()[variable_name]
                return obj.unit() if hasattr(obj, 'unit') else ''
            if variable_name in self.data.constants():
                obj = self.data.constants()[variable_name]
                return obj.unit() if hasattr(obj, 'unit') else ''
        except Exception:
            pass
        return ''

    def get_results(self, variables_list_of_lists, flatten=False):
        """
        gets results after a simulation
        inputs:
        obs_names: list of list of strings, stores the names of state, algebraic, and constant variables you wish to access
        outputs:
        results: list of lists where the first index is the observable index
        and the second is the operand index for that observable. The same shape as
        the input (except list inputs get turned into list of lists).
        Each entry can be float or numpy array
        """
        if type(variables_list_of_lists[0]) is not list:
            variables_list_of_lists = [[entry] for entry in variables_list_of_lists]

        results = []
        valid_states = self.list_states()
        valid_algebraics = self.list_algebraics()
        valid_constants = self.list_constants()

        for JJ, variables_list in enumerate(variables_list_of_lists):
            results.append([])
            for variable_name in variables_list:
                if variable_name == 'time':
                    results[JJ].append(self.tSim)
                elif variable_name in self.simulation.results().states():
                    results[JJ].append(self.simulation.results().states()[variable_name].values()[-self.n_steps - 1:].copy())
                elif variable_name in self.simulation.results().algebraic():
                    results[JJ].append(self.simulation.results().algebraic()[variable_name].values()[-self.n_steps - 1:].copy())
                elif variable_name in self.data.constants():
                    results[JJ].append(self.data.constants()[variable_name])
                else:
                    raise KeyError(
                        f"variable {variable_name} is not a model variable.\n"
                        f"states:\n{valid_states}\n\n"
                        f"algebraics:\n{valid_algebraics}\n\n"
                        f"constants:\n{valid_constants}"
                    )

        if flatten:
            results = [item for sublist in results for item in sublist]
        return results

    def get_init_param_vals(self, param_names):
        param_init = []
        valid_states = [name for name in self.data.states()]
        valid_constants = [name for name in self.data.constants()]

        for JJ, param_name_or_list in enumerate(param_names):
            if isinstance(param_name_or_list, list):
                param_init.append([])
                for param_name in param_name_or_list:
                    if param_name in self.data.states():
                        param_init[JJ].append(self.data.states()[param_name])
                    elif param_name in self.data.constants():
                        param_init[JJ].append(self.data.constants()[param_name])
                    else:
                        raise KeyError(
                            f"parameter name {param_name} doesn't exist in either constants or states.\n"
                            f"states:\n{valid_states}\n\nconstants:\n{valid_constants}"
                        )
            else:
                param_name = param_name_or_list
                if param_name in self.data.states():
                    param_init.append(self.data.states()[param_name])
                elif param_name in self.data.constants():
                    param_init.append(self.data.constants()[param_name])
                else:
                    raise KeyError(
                        f"parameter name {param_name} doesn't exist in either constants or states.\n"
                        f"states:\n{valid_states}\n\nconstants:\n{valid_constants}"
                    )

        return param_init

    def set_param_vals(self, param_names, param_vals):
        valid_states = [name for name in self.data.states()]
        valid_constants = [name for name in self.data.constants()]

        for JJ, param_name_or_list in enumerate(param_names):
            if isinstance(param_name_or_list, list):
                for param_name in param_name_or_list:
                    if param_name in self.data.states():
                        self.data.states()[param_name] = param_vals[JJ]
                    elif param_name in self.data.constants():
                        self.data.constants()[param_name] = param_vals[JJ]
                    else:
                        raise KeyError(
                            f"parameter name {param_name} doesn't exist in either constants or states.\n"
                            f"states:\n{valid_states}\n\nconstants:\n{valid_constants}"
                        )
            else:
                param_name = param_name_or_list
                if param_name in self.data.states():
                    self.data.states()[param_name] = param_vals[JJ]
                elif param_name in self.data.constants():
                    self.data.constants()[param_name] = param_vals[JJ]
                else:
                    raise KeyError(
                        f"parameter name {param_name} doesn't exist in either constants or states.\n"
                        f"states:\n{valid_states}\n\nconstants:\n{valid_constants}"
                    )

    def modify_params_and_run_and_get_results(self, param_names, mod_factors, obs_names, absolute=False):

        if absolute:
            new_param_vals = mod_factors
        else:
            init_param_vals = self.get_init_param_vals(param_names)
            new_param_vals = [a * b for a, b in zip(init_param_vals, mod_factors)]

        print(new_param_vals)
        self.set_param_vals(param_names, new_param_vals)

        success = self.run()
        if success:
            pred_obs_new = self.get_results(obs_names)
            self.reset_and_clear()
        else:
            raise RuntimeError('simulation failed')

        return pred_obs_new

    def update_times(self, dt, start_time, sim_time, pre_time):
        self.dt = dt
        self.stop_time = start_time + pre_time + sim_time  # full time of simulation
        self.pre_steps = int(pre_time / self.dt)  # number of steps to do before storing data (used to reach steady state)
        self.n_steps = int(sim_time / self.dt)  # number of steps for storing data
        self.data.set_starting_point(start_time)
        self.data.set_ending_point(self.stop_time)
        self.tSim = np.linspace(start_time + pre_time, self.stop_time, self.n_steps + 1)  # time values for stored part of simulation

    def close_simulation(self):
        oc.close_simulation(self.simulation)
