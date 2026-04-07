#!/usr/bin/env python3
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from opencor_helper import SimulationHelper


# ---------------- user settings ----------------
CELLML_FILE = "/home/sliu205/0D_hemodynamics_paper/Preliminary_results/generated_models/H_D_network/H_D_network.cellml"

DT = 0.2
CHANGE_TIME = 100.0
TOTAL_TIME = 200.0
POST_TIME = TOTAL_TIME - CHANGE_TIME

PRE_TIME = 0.0
SOLVER_INFO = {'MaximumStep': 0.2, 'MaximumNumberOfSteps': 10000}

OUTPUT_DIR = "cellml_run_outputs"

TC_INDICES = range(1, 7)
HMEAN_VARS = [f"TC{i}/H_mean" for i in TC_INDICES]
V_VARS = [f"TC{i}/v" for i in TC_INDICES]

TRACKED_VARS = HMEAN_VARS + V_VARS
# ------------------------------------------------


def as_series(result_item, time):
    x = result_item[0]

    if isinstance(x, np.ndarray):
        return x

    if hasattr(x, "__len__") and not isinstance(x, (float, int)):
        return np.asarray(x)

    return np.full(len(time), float(x))


def get_series_dict(helper, variables):
    results = helper.get_results(['time'] + variables)
    time = np.asarray(results[0][0])

    data = {}
    for i, var in enumerate(variables, start=1):
        data[var] = as_series(results[i], time)

    return time, data


def capture_state_snapshot(helper):

    state_names = list(helper.data.states())
    state_values = []

    for s in state_names:
        state_values.append(helper.simulation.results().states()[s].values()[-1])

    return state_names, state_values


def run_segment(start_time, sim_time, init_states=None, param_changes=None):

    helper = SimulationHelper(
        CELLML_FILE,
        DT,
        sim_time,
        solver_info=SOLVER_INFO,
        pre_time=PRE_TIME,
    )

    helper.update_times(DT, start_time, sim_time, PRE_TIME)

    if init_states is not None:
        names, values = init_states
        helper.set_param_vals(names, values)

    if param_changes:
        names = list(param_changes.keys())
        vals = list(param_changes.values())
        helper.set_param_vals(names, vals)

    success = helper.run()
    if not success:
        helper.close_simulation()
        raise RuntimeError("Simulation failed.")

    time, data = get_series_dict(helper, TRACKED_VARS)

    snapshot = capture_state_snapshot(helper)

    const_vals = {}
    for cname in ["PV01/r", "PV03/r"]:
        if cname in helper.data.constants():
            const_vals[cname] = float(helper.data.constants()[cname])

    helper.close_simulation()

    return time, data, snapshot, const_vals


def stitch_segments(time_pre, data_pre, time_post, data_post):

    full_time = np.concatenate([time_pre, time_post[1:]])

    full_data = {}
    for var in data_pre:
        full_data[var] = np.concatenate([data_pre[var], data_post[var][1:]])

    return full_time, full_data


def write_csv(path, time, baseline, pv01, pv03):

    with open(path, "w") as f:

        header = ["time"]
        for var in TRACKED_VARS:
            header += [
                f"{var}_baseline",
                f"{var}_PV01",
                f"{var}_PV03"
            ]

        f.write(",".join(header) + "\n")

        for i in range(len(time)):
            row = [str(time[i])]
            for var in TRACKED_VARS:
                row.append(str(baseline[var][i]))
                row.append(str(pv01[var][i]))
                row.append(str(pv03[var][i]))
            f.write(",".join(row) + "\n")


def plot_group(time, variables, baseline, pv01, pv03, ylabel, title, outpath):

    fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharex=True)
    axes = axes.flatten()

    for ax, var in zip(axes, variables):

        ax.plot(time, baseline[var], label="baseline")
        ax.plot(time, pv01[var], label="PV01/r × 0.3")
        ax.plot(time, pv03[var], label="PV03/r × 0.3")

        ax.axvline(CHANGE_TIME, linestyle="--", linewidth=1)

        ax.set_title(var)
        ax.set_ylabel(ylabel)
        ax.grid(True)

    for ax in axes[-2:]:
        ax.set_xlabel("Time")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3)

    fig.suptitle(title)
    fig.tight_layout(rect=[0,0,1,0.95])

    fig.savefig(outpath, dpi=300)
    plt.close()


def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Running baseline 0 → 100")

    time_pre, data_pre, snapshot_t100, consts = run_segment(
        start_time=0,
        sim_time=CHANGE_TIME
    )

    pv01_base = consts["PV01/r"]
    pv03_base = consts["PV03/r"]

    print("Running baseline branch")

    time_post_base, data_post_base, _, _ = run_segment(
        start_time=CHANGE_TIME,
        sim_time=POST_TIME,
        init_states=snapshot_t100
    )

    print("Running PV01 change branch")

    time_post_pv01, data_post_pv01, _, _ = run_segment(
        start_time=CHANGE_TIME,
        sim_time=POST_TIME,
        init_states=snapshot_t100,
        param_changes={"PV01/r": pv01_base * 0.3}
    )

    print("Running PV03 change branch")

    time_post_pv03, data_post_pv03, _, _ = run_segment(
        start_time=CHANGE_TIME,
        sim_time=POST_TIME,
        init_states=snapshot_t100,
        param_changes={"PV03/r": pv03_base * 0.3}
    )

    full_time, baseline_full = stitch_segments(time_pre, data_pre, time_post_base, data_post_base)
    _, pv01_full = stitch_segments(time_pre, data_pre, time_post_pv01, data_post_pv01)
    _, pv03_full = stitch_segments(time_pre, data_pre, time_post_pv03, data_post_pv03)

    csv_path = os.path.join(OUTPUT_DIR, "comparison_TC1_TC6.csv")

    write_csv(csv_path, full_time, baseline_full, pv01_full, pv03_full)

    plot_group(
        full_time,
        HMEAN_VARS,
        baseline_full,
        pv01_full,
        pv03_full,
        ylabel="H_mean",
        title="H_mean comparison",
        outpath=os.path.join(OUTPUT_DIR, "H_mean_comparison.png")
    )

    plot_group(
        full_time,
        V_VARS,
        baseline_full,
        pv01_full,
        pv03_full,
        ylabel="velocity",
        title="velocity comparison",
        outpath=os.path.join(OUTPUT_DIR, "velocity_comparison.png")
    )

    print("\nDone")
    print("CSV:", csv_path)


if __name__ == "__main__":
    main()
