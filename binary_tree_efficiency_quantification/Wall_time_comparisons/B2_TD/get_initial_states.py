"""
get_initial_states.py
=====================
Opens a CellML model via opencor_helper, runs a minimal simulation so that
algebraic variables are populated, then writes a CSV containing:
  - every initial state variable        (category: state)
  - every constant                      (category: constant)
  - every algebraic variable at t=0     (category: algebraic)

Usage:
    python get_initial_states.py path/to/model.cellml

The output CSV is written next to this script as  initial_params.csv
"""

import sys
import csv
import os
from opencor_helper import SimulationHelper


# ============================================================
# CONFIG  –  edit these if you are not passing args on the CLI
# ============================================================

DEFAULT_CELLML = "B2_TD.cellml"   # fallback if no CLI argument given
DT             = 0.0001            # time-step
SIM_TIME       =0.001        # minimal sim time – just enough to populate algebraic vars
OUTPUT_CSV     = "initial_params.csv"


# ============================================================
# RESOLVE CELLML PATH
# ============================================================

cellml_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CELLML

if not os.path.isfile(cellml_path):
    print(f"ERROR: CellML file not found: {cellml_path}")
    sys.exit(1)

print(f"Opening model: {cellml_path}")


# ============================================================
# OPEN SIMULATION AND RUN MINIMALLY
# (run is required so that algebraic variables get populated)
# ============================================================

helper = SimulationHelper(
    cellml_path = cellml_path,
    dt          = DT,
    sim_time    = SIM_TIME,
)

data       = helper.data
simulation = helper.simulation

print("Running minimal simulation to populate algebraic variables...")
success = helper.run()
if not success:
    print("ERROR: Simulation failed to converge even for minimal run. Exiting.")
    sys.exit(1)
print("Simulation complete.")


# ============================================================
# COLLECT ALL STATE VARIABLES (initial value = first result)
# ============================================================

rows = []

print("Reading initial state variables...")
for name in simulation.results().states():
    try:
        # .values()[0] is the value at t=0 (the initial state)
        value = simulation.results().states()[name].values()[-1]#change to value = simulation.results().algebraic()[name].values()[-1] for final timestep values for intial states, 0 for proper initial value (some are 0)
    except Exception as e:
        # Fall back to the data object if results aren't available
        try:
            value = data.states()[name]
        except Exception as e2:
            value = f"ERROR: {e} / {e2}"
    rows.append({
        "category" : "state",
        "variable" : name,
        "value"    : value,
    })

n_states = sum(1 for r in rows if r["category"] == "state")
print(f"  Found {n_states} state variables.")


# ============================================================
# COLLECT ALL CONSTANTS
# ============================================================

constants_start = len(rows)

print("Reading constants...")
for name in data.constants():
    try:
        value = data.constants()[name]
    except Exception as e:
        value = f"ERROR: {e}"
    rows.append({
        "category" : "constant",
        "variable" : name,
        "value"    : value,
    })

n_constants = len(rows) - constants_start
print(f"  Found {n_constants} constants.")


# ============================================================
# COLLECT ALL ALGEBRAIC VARIABLES (value at t=0)
# ============================================================

algebraic_start = len(rows)

print("Reading algebraic variables...")
for name in simulation.results().algebraic():
    try:
        # .values()[0] is the algebraic value at the first time point
        value = simulation.results().algebraic()[name].values()[-1] #change to value = simulation.results().algebraic()[name].values()[-1] for final timestep values for intial states, 0 for proper initial value (some are 0)
    except Exception as e:
        value = f"ERROR: {e}"
    rows.append({
        "category" : "algebraic",
        "variable" : name,
        "value"    : value,
    })

n_algebraic = len(rows) - algebraic_start
print(f"  Found {n_algebraic} algebraic variables.")


# ============================================================
# WRITE CSV
# ============================================================

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), OUTPUT_CSV)

with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "variable", "value"])
    writer.writeheader()
    writer.writerows(rows)

print(f"\nCSV saved to: {output_path}")
print(f"Total rows written: {len(rows)}")
print(f"  States:    {n_states}")
print(f"  Constants: {n_constants}")
print(f"  Algebraic: {n_algebraic}")


# ============================================================
# CLEAN UP
# ============================================================

helper.close_simulation()