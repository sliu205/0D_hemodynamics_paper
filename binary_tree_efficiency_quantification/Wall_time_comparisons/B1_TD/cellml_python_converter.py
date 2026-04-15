"""
Simple starter script to convert CellML cardiovascular model to Python.

This script:
1. Parses CellML parameter files to extract values and units
2. Sets up the ODE system structure
3. Provides a framework for adding equations from the modules
"""

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Dict, List, Tuple
import numpy as np
from scipy.integrate import solve_ivp


# ============================================================================
# STEP 1: Parse CellML Parameters
# ============================================================================

@dataclass
class Parameter:
    """A single parameter with name, value, and units."""
    name: str
    value: float
    units: str


def parse_cellml_parameters(filename: str) -> Dict[str, Parameter]:
    """
    Parse parameters from a CellML file, scoping them by component name.
    
    Returns:
        Dictionary mapping "component:param_name" -> Parameter object
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Define namespace
    ns = {'cellml': 'http://www.cellml.org/cellml/1.1#'}
    
    parameters = {}
    
    # Find all variables in all components, with component context
    for component in root.findall('.//cellml:component', ns):
        comp_name = component.get('name')
        
        for var in component.findall('cellml:variable', ns):
            var_name = var.get('name')
            initial_value = var.get('initial_value')
            units = var.get('units')
            
            if initial_value is not None and var_name is not None:
                try:
                    value = float(initial_value)
                    # Scope parameters by component name
                    scoped_name = f"{comp_name}:{var_name}" if comp_name else var_name
                    parameters[scoped_name] = Parameter(
                        name=scoped_name,
                        value=value,
                        units=units if units else 'unknown'
                    )
                except ValueError:
                    pass  # Skip non-numeric values
    
    return parameters


# ============================================================================
# STEP 2: Load All Parameters
# ============================================================================

def load_model_parameters(param_file: str, global_file: str) -> Dict[str, float]:
    """
    Load all parameters from both parameter files.
    
    Args:
        param_file: Path to B1_TD_parameters.cellml
        global_file: Path to same file (parameters_global component)
    
    Returns:
        Flat dictionary of parameter_name -> value
    """
    params = {}
    
    # Parse both parameter components from the same file
    param_dict = parse_cellml_parameters(param_file)
    
    for name, param in param_dict.items():
        params[name] = param.value
    
    return params


# ============================================================================
# STEP 3: Model Structure
# ============================================================================

class VesselComponent:
    """Base class for a vessel/junction component."""
    
    def __init__(self, name: str, initial_state: List[float]):
        """
        Args:
            name: Component name (e.g., 'inlet', 'PV1')
            initial_state: List of initial ODE variables
        """
        self.name = name
        self.state = initial_state  # State variables [y1, y2, ...]
        self.inputs = {}  # Connected variables from other components
    
    def compute_state_derivatives(self, t: float) -> List[float]:
        """
        Compute d(state)/dt for this component.
        
        This is where you add the actual differential equations.
        For now, returns zeros as placeholder.
        """
        return [0.0] * len(self.state)


class CardiovascularModel:
    """
    Main ODE model for the cardiovascular system.
    
    Manages all components, connections, and integration.
    """
    
    def __init__(self, params: Dict[str, float]):
        """
        Initialize model with parameters.
        
        Args:
            params: Dictionary of parameter values (scoped as "component:name")
        """
        self.params = params
        self.components: Dict[str, VesselComponent] = {}
        self.connections: List[Tuple[str, str, str, str]] = []
        self.vessel_names = [
            'inlet_module',      # Inlet capillary
            'VV_junc1_module',   # Vessel-vessel junction 1
            'PV1_module',        # Parent-pericyte 1
            'PV2_module',        # Parent-pericyte 2
            'V1_module',         # Vessel 1
            'V2_module',         # Vessel 2
        ]
        
    def add_component(self, name: str, component: VesselComponent):
        """Register a component in the model."""
        self.components[name] = component
    
    def add_connection(self, comp1: str, var1: str, comp2: str, var2: str):
        """
        Register a connection between two components.
        
        This means: comp1.var1 is connected to comp2.var2
        (they should have the same value at each time step)
        """
        self.connections.append((comp1, var1, comp2, var2))
    
    def get_vessel_params(self, vessel_name: str) -> Dict[str, float]:
        """
        Extract all parameters for a specific vessel.
        
        Args:
            vessel_name: Name like 'inlet_module', 'PV1_module', etc.
        
        Returns:
            Dictionary of param_name -> value for that vessel
        """
        vessel_params = {}
        prefix = f"{vessel_name}:"
        
        for scoped_name, param in self.params.items():
            if scoped_name.startswith(prefix):
                # Remove the prefix
                param_name = scoped_name[len(prefix):]
                vessel_params[param_name] = param.value
        
        # Also add global parameters (from parameters_global component)
        global_prefix = "parameters_global:"
        for scoped_name, param in self.params.items():
            if scoped_name.startswith(global_prefix):
                param_name = scoped_name[len(global_prefix):]
                vessel_params[param_name] = param.value
        
        return vessel_params
    
    def print_vessel_parameters(self):
        """Pretty-print all parameters organized by vessel."""
        print("\n" + "=" * 80)
        print("PARAMETERS BY VESSEL")
        print("=" * 80)
        
        for vessel_name in self.vessel_names:
            vessel_params = self.get_vessel_params(vessel_name)
            
            if vessel_params:
                print(f"\n{vessel_name}:")
                print("-" * 80)
                for param_name, value in sorted(vessel_params.items()):
                    # Find units from original parameter
                    scoped_name = f"{vessel_name}:{param_name}"
                    units = self.params[scoped_name].units if scoped_name in self.params else "unknown"
                    print(f"  {param_name:30s} = {value:20.6e}  ({units})")
    
    def rhs(self, t: float, y: np.ndarray) -> np.ndarray:
        """
        Right-hand side of the ODE system.
        
        Args:
            t: Current time
            y: Current state vector (flattened across all components)
        
        Returns:
            dy/dt: Time derivatives
        """
        dydt = []
        
        # For now, just return zeros (placeholder)
        # You would:
        # 1. Split y into states for each component
        # 2. Call compute_state_derivatives for each
        # 3. Apply connections (algebraic constraints)
        # 4. Concatenate results
        
        return np.zeros_like(y)
    
    def solve(self, t_span: Tuple[float, float], t_eval: np.ndarray, 
              y0: np.ndarray):
        """
        Integrate the ODE system.
        
        Args:
            t_span: (t_start, t_end)
            t_eval: Times at which to report solution
            y0: Initial conditions
        
        Returns:
            Solution object from scipy
        """
        sol = solve_ivp(
            self.rhs,
            t_span,
            y0,
            t_eval=t_eval,
            method='RK45',
            dense_output=True
        )
        return sol


# ============================================================================
# STEP 4: Quick Test
# ============================================================================

if __name__ == '__main__':
    # Parse parameters
    print("Loading parameters...")
    params = load_model_parameters(
        'B1_TD_parameters.cellml',
        'B1_TD_parameters.cellml'
    )
    
    # Initialize model
    print(f"\nInitializing model...")
    model = CardiovascularModel(params)
    
    # Show all parameters organized by vessel
    model.print_vessel_parameters()
    
    # Example: Add components for each vessel
    print(f"\n" + "=" * 80)
    print("MODEL STRUCTURE")
    print("=" * 80)
    
    for vessel_name in model.vessel_names:
        vessel_params = model.get_vessel_params(vessel_name)
        if vessel_params:
            inlet = VesselComponent(vessel_name, initial_state=[0.0])
            model.add_component(vessel_name, inlet)
            print(f"✓ Added component: {vessel_name:25s} ({len(vessel_params)} parameters)")
    
    print(f"\nTotal components: {len(model.components)}")
    print(f"Total connections: {len(model.connections)}")
    
    # Example: Simple integration (all zeros for now)
    print(f"\n" + "=" * 80)
    print("TEST INTEGRATION")
    print("=" * 80)
    print("\nRunning test integration (0 to 1 second)...")
    t_eval = np.linspace(0, 1, 100)
    y0 = np.array([0.0])  # One state variable
    
    sol = model.solve((0, 1), t_eval, y0)
    
    print(f"Integration complete. Solution shape: {sol.y.shape}")
    print(f"Time range: {sol.t[0]:.3f} to {sol.t[-1]:.3f} seconds")