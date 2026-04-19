# ============================================================
# WEEK 9 — Student Assignment
# AP CSP + VEX V5 Robotics Integration
# Loops & Iteration: Going Deeper
#
# Name: Taylor
# Tutor: Jonathan Contreras
# ============================================================
#
# HOW TO USE THIS FILE:
#   1. Read every comment carefully before writing any code.
#   2. Sketch pseudocode on paper before typing for TODO 4.
#   3. Run the file often — it will tell you which TODO is next.
#   4. The reflection questions at the bottom are required.
#      Write full sentences, just like the AP written response.
#
# GRADING FOCUS (what Jonathan is looking for):
#   - Correct accumulator initialization (before the loop!)
#   - Loop terminates correctly in all cases
#   - break and continue used where described
#   - Autonomous loop uses time-based condition
#   - Reflection answers are complete sentences
# ============================================================

import time
import random

random.seed(99)   # keep results consistent

print("Week 9 Assignment — Taylor")
print("=" * 55)
print()


# ============================================================
# SIMULATION HELPERS
# (Same pattern as the live coding file.)
# ============================================================

SENSOR_LOG_A = [18.2, 5.1, -1, 22.7, -1, 11.4, 9.8, -1, 16.3, 20.0]
SENSOR_LOG_B = [-1, -1, -1, -1]   # all errors — edge case!
SENSOR_LOG_C = [8.0, 14.5, 7.3, 11.1, 9.6]   # no errors

ZONE_DATA = [
    {"name": "Alpha",   "color": "blue",  "active": True},
    {"name": "Beta",    "color": "none",  "active": False},
    {"name": "Gamma",   "color": "green", "active": True},
    {"name": "Delta",   "color": "red",   "active": True},
    {"name": "Epsilon", "color": "none",  "active": False},
    {"name": "Zeta",    "color": "blue",  "active": True},
    {"name": "Eta",     "color": "green", "active": False},
]

GRID_5x5 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],   # object at row 2, col 3
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def obstacle_ahead():
    return random.random() < 0.25

def object_in_range():
    return random.random() < 0.20

def hazard_detected():
    return random.random() < 0.15

def drive_forward(inches):
    print(f"    [MOTOR] Driving {inches} in.")

def turn_right(degrees):
    print(f"    [MOTOR] Turning right {degrees}°.")

def collect_object():
    print(f"    [CLAW] Object collected.")

def activate_alarm():
    print(f"    [ALARM] Hazard alarm activated.")

def stop_motors():
    print(f"    [MOTOR] Stopped.")


# ============================================================
# TODO 1 — Accumulator Toolbox
# ============================================================
#
# Write four functions that each use the accumulator pattern.
# Each function takes a list of sensor readings as input.
# Error values are -1 — skip them in every function.
#
# You will test each function against the three SENSOR_LOGs
# defined above, including SENSOR_LOG_B which is all errors.
# ============================================================

print("-" * 55)
print("TODO 1: Accumulator Toolbox")
print("-" * 55)
print()

# ----------------------------------------------------------
# TODO 1a: calculate_average(readings)
#
# Return the average of all valid readings (not -1).
# If there are NO valid readings, return None (don't crash!).
#
# Hint: you need two accumulators — a total and a count.
# ----------------------------------------------------------

def calculate_average(readings):
    starting_distance = 0 #starts everyhthing on a basic level
    valid_count = 0             # ← initialize

    for reading in readings:
        if reading != -1:       # skip error values
            starting_distance += reading
            valid_count += 1   # ← update INSIDE the loop
    if valid_count == 0:         # check for zero valid readings
        return None
    average = starting_distance / valid_count
    return average

    """
   
    Returns:
        float: average of valid readings, or None if none exist
    """
    # TODO: initialize your accumulators here

    # TODO: return the average, or None if no valid readings were found


# ----------------------------------------------------------
# TODO 1b: find_maximum(readings)
#
# Return the largest valid reading.
# If there are NO valid readings, return None.
#
# Do NOT use Python's built-in max() function.
# Write it yourself using the accumulator pattern.
# ----------------------------------------------------------

def find_maximum(readings):
    starting_distance = 0 #starts everyhthing on a basic level
    valid_count = 0  
    for reading in readings:
        if reading != -1:       # skip error values
            if starting_distance > reading:
                starting_distance = starting_distance
            else:
                starting_distance = reading
                valid_count += 1   # ← update INSIDE the loop
    if valid_count == 0:         # check for zero valid readings
        return None
    return starting_distance 

    """
    Find the largest valid sensor reading.

    Parameters:
        readings (list): list of floats; -1 = error

    Returns:
        float: largest valid reading, or None if none exist
    """

# ----------------------------------------------------------
# TODO 1c: count_above_threshold(readings, threshold)
#
# Return the count of valid readings that are STRICTLY
# greater than the threshold value.
#
# Example: count_above_threshold([5.0, 12.0, -1, 8.0], 9.0)
# → should return 1  (only 12.0 is above 9.0)
# ----------------------------------------------------------

def count_above_threshold(readings, threshold):
    starting_count = 0
    for reading in readings:
        if reading != -1:       # skip error values
            if reading > threshold:
                starting_count += 1   # ← update INSIDE the loop
    return starting_count
    """
    Count valid readings above a given threshold.

    Parameters:
        readings (list): list of floats; -1 = error
        threshold (float): cutoff value

    Returns:
        int: number of valid readings strictly greater than threshold
    """
    # TODO: write this function


# ----------------------------------------------------------
# TODO 1d: collect_valid(readings)
#
# Return a NEW list containing only the valid readings.
# The original list must not be modified.
#
# Example: collect_valid([10.0, -1, 8.5, -1]) → [10.0, 8.5]
# ----------------------------------------------------------

def collect_valid(readings):
    valid_readings = []         # ← initialize to empty list
    for reading in readings:
        if reading != -1:
            valid_readings.append(reading)   # ← update: add to the list
    return valid_readings

# --- Test your functions ---

print("Testing with SENSOR_LOG_A (has errors):")
print(f"  Log A: {SENSOR_LOG_A}")
print(f"  Average:   {calculate_average(SENSOR_LOG_A)}")
print(f"  Maximum:   {find_maximum(SENSOR_LOG_A)}")
print(f"  Above 15:  {count_above_threshold(SENSOR_LOG_A, 15.0)}")
print(f"  Valid list: {collect_valid(SENSOR_LOG_A)}")
print()

print("Testing with SENSOR_LOG_B (ALL errors — edge case!):")
print(f"  Log B: {SENSOR_LOG_B}")
print(f"  Average:   {calculate_average(SENSOR_LOG_B)}")
print(f"  Maximum:   {find_maximum(SENSOR_LOG_B)}")
print(f"  Above 10:  {count_above_threshold(SENSOR_LOG_B, 10.0)}")
print(f"  Valid list: {collect_valid(SENSOR_LOG_B)}")
print()

print("Testing with SENSOR_LOG_C (no errors):")
print(f"  Log C: {SENSOR_LOG_C}")
print(f"  Average:   {calculate_average(SENSOR_LOG_C)}")
print(f"  Maximum:   {find_maximum(SENSOR_LOG_C)}")
print(f"  Above 10:  {count_above_threshold(SENSOR_LOG_C, 10.0)}")
print(f"  Valid list: {collect_valid(SENSOR_LOG_C)}")
print()

input("Press Enter for TODO 2...")
print()


# ============================================================
# TODO 2 — List Builder + Filtered Search
# ============================================================
#
# Work with ZONE_DATA (defined above — 7 zones with name,
# color, and active status).
# ============================================================

print("-" * 55)
print("TODO 2: List Builder + Filtered Search")
print("-" * 55)
print()

# ----------------------------------------------------------
# TODO 2a: build_active_zone_names()
#
# Return a list of NAMES of all zones where active == True.
# ----------------------------------------------------------

def build_active_zone_names(zones):
    active_names = []         # ← initialize to empty list
    for zone in zones:
       if zone["active"] == True:  # check if zone is active
            active_names.append(zone["name"])  # ← update: add the name to the list
    return active_names

    """
    Return a list of names of all active zones.

    Parameters:
        zones (list of dicts): the zone data

    Returns:
        list of str: names of zones where active is True
    """
    # TODO: write this function (use a list accumulator)


# ----------------------------------------------------------
# TODO 2b: find_zone_by_color(zones, target_color)
#
# Return the NAME of the FIRST zone that matches target_color.
# Use break to stop as soon as you find it.
# If no zone has that color, return None.
#
# This is an efficient linear search.
# ----------------------------------------------------------

def find_zone_by_color(zones, target_color):
    found_zone = None           # ← we haven't found anything yet
    for zone in zones:
        if zone["color"] == target_color:
            found_zone = zone["name"]
            # Problem: the loop KEEPS GOING even after we find it!
            # We'll fix this in Part 3 with break.
            break   # ← this will exit the loop immediately after finding the match
    return found_zone

# --- Test ---

print(f"Zone data: {len(ZONE_DATA)} zones loaded.")
print()
print(f"Active zone names: {build_active_zone_names(ZONE_DATA)}")
print()
print(f"First 'blue' zone:  {find_zone_by_color(ZONE_DATA, 'blue')}")
print(f"First 'green' zone: {find_zone_by_color(ZONE_DATA, 'green')}")
print(f"First 'red' zone:   {find_zone_by_color(ZONE_DATA, 'red')}")
print(f"First 'purple' zone: {find_zone_by_color(ZONE_DATA, 'purple')}  ← should be None")
print()

input("Press Enter for TODO 3...")
print()


# ============================================================
# TODO 3 — Grid Search with break and Flag Variable
# ============================================================
#
# Search GRID_5x5 for the object (cell value = 1).
# The grid is 5 rows × 5 columns.
#
# Requirements:
#   - Use a nested loop (outer = rows, inner = columns)
#   - Use a flag variable to exit both loops once found
#   - Count how many cells you checked before finding it
#   - If object not found, say so clearly
# ============================================================

print("-" * 55)
print("TODO 3: Grid Search with Flag Variable")
print("-" * 55)
print()

def search_grid(grid):
    """
    Search a 2D grid for an object (cell value = 1).

    Parameters:
        grid (list of lists): 2D grid of 0s and 1s

    Returns:
        tuple: (found_row, found_col, cells_checked)
               found_row and found_col are None if not found
    """
    found_row    = None
    found_col    = None
    cells_checked = 0
    # TODO: initialize your flag variable here

    # TODO: write the nested loop
    # Outer loop: iterate over rows using enumerate()
    # Inner loop: iterate over columns using enumerate()
    # Inside inner loop:
    #   - increment cells_checked
    #   - check if cell == 1
    #   - if found: set found_row, found_col, flag, and break
    # After inner loop: check flag and break outer if needed

    return found_row, found_col, cells_checked


# --- Test ---

print("Searching GRID_5x5:")
for i, row in enumerate(GRID_5x5):
    print(f"  Row {i}: {row}")
print()

row, col, checked = search_grid(GRID_5x5)

if row is not None:
    print(f"Object found at row {row}, col {col}.")
else:
    print("Object not found in grid.")

total_cells = len(GRID_5x5) * len(GRID_5x5[0])
print(f"Checked {checked} of {total_cells} cells.")
print()

input("Press Enter for TODO 4...")
print()


# ============================================================
# TODO 4 — Timed Autonomous Routine
# ============================================================
#
# Write a complete autonomous routine that runs for
# AUTONOMOUS_DURATION seconds.
#
# ⭐ IMPORTANT: Sketch your decision logic on paper FIRST.
#    Draw a flowchart showing what the robot does in each case.
#    Then translate that into code.
#
# Decision priority (implement in this order):
#   1. If hazard_detected()  → activate_alarm()
#   2. Elif obstacle_ahead() → turn_right(30)
#   3. Elif object_in_range() → collect_object()
#   4. Else                  → drive_forward(4)
#
# Track these metrics with accumulators:
#   - hazards_found      (int)
#   - obstacles_avoided  (int)
#   - objects_collected  (int)
#   - distance_traveled  (float) — add 4.0 when driving forward
#   - total_actions      (int) — count every iteration
#
# Print a report after the loop ends.
#
# Use AUTONOMOUS_DURATION = 3.0 seconds for testing.
# ============================================================

print("-" * 55)
print("TODO 4: Timed Autonomous Routine")
print("-" * 55)
print()

AUTONOMOUS_DURATION = 3.0

def run_autonomous():
    """Run a timed autonomous routine and print a performance report."""

    print(f"Starting {AUTONOMOUS_DURATION}s autonomous run...")
    print()

    # TODO: initialize all accumulator variables here

    # TODO: record start_time with time.time()

    # TODO: write the timed while loop
    # Condition: time.time() - start_time < AUTONOMOUS_DURATION
    # Inside the loop:
    #   - calculate elapsed = round(time.time() - start_time, 2)
    #   - implement the priority decision chain
    #   - update the right accumulator for each action
    #   - call time.sleep(0.4) at the end of each iteration

    stop_motors()
    print()

    # TODO: print the performance report
    # Include all five metrics.
    # Format it clearly — label each value.
    print("-" * 45)
    print("AUTONOMOUS REPORT")
    print("-" * 45)
    # your print statements here


run_autonomous()
print()

input("Press Enter for TODO 5 (Bonus)...")
print()


# ============================================================
# TODO 5 — BONUS: continue in a Processing Loop
# ============================================================
#
# This TODO is optional but good AP exam practice.
#
# Write a function process_log(readings, threshold) that:
#   - Skips error readings (-1) using continue
#   - Skips readings BELOW threshold using continue
#   - For remaining readings: print them and add to a total
#   - Returns the total at the end
#
# Example:
#   process_log([5.0, -1, 12.0, 3.0, 15.0], 8.0)
#   → should process 12.0 and 15.0 (skips -1, 5.0, and 3.0)
#   → returns 27.0
# ============================================================

print("-" * 55)
print("TODO 5 (BONUS): continue in a Processing Loop")
print("-" * 55)
print()

def process_log(readings, threshold):
    """
    Process sensor readings, skipping errors and below-threshold values.

    Parameters:
        readings (list): sensor readings; -1 = error
        threshold (float): minimum valid value to process

    Returns:
        float: sum of all processed readings
    """
    # TODO: write this function using continue for both skip conditions


# --- Test ---
test_readings = [5.0, -1, 12.0, 3.0, -1, 15.0, 8.5, 7.9, -1, 20.0]
print(f"Input: {test_readings}")
print(f"Threshold: 8.0")
result = process_log(test_readings, 8.0)
print(f"Total of processed readings: {result}")
print(f"(Expected: 12.0 + 15.0 + 8.5 + 20.0 = 55.5)")
print()

input("Press Enter for Reflection Questions...")
print()


# ============================================================
# REFLECTION QUESTIONS
# ============================================================
#
# Answer these in the triple-quoted strings below.
# Write in FULL SENTENCES — this is AP written response practice.
# One or two sentences per question is fine.
# These are NOT multiple choice. Explain your thinking.
# ============================================================

print("-" * 55)
print("Reflection Questions")
print("-" * 55)
print()

Q1 = """
Q1: What is the accumulator pattern?
Describe it in your own words — what do you do before the loop,
inside the loop, and after the loop? Give one real example.

YOUR ANSWER:

"""

Q2 = """
Q2: What is the difference between 'break' and 'continue'?
Give one example of when you'd use each one in a program.

YOUR ANSWER:

"""

Q3 = """
Q3: In your autonomous routine (TODO 4), identify one place where
ITERATION and SELECTION work together. Describe what that code
does and why both are necessary for the robot's purpose.

YOUR ANSWER:

"""

Q4 = """
Q4: In the grid search (TODO 3), what is the WORST CASE number of
cells your loop checks? What is the BEST CASE? Explain why the
difference matters when the grid is very large.

YOUR ANSWER:

"""

Q5 = """
Q5 (AP Connection): The AP Create Task asks you to describe a place
in your program where a list is being used and why the list was needed.
Look at your collect_valid() function from TODO 1d. Write 2–3 sentences
explaining what the list stores, how the loop populates it, and what
would be harder (or impossible) without using a list.

YOUR ANSWER:

"""

print(Q1)
print(Q2)
print(Q3)
print(Q4)
print(Q5)

print("=" * 55)
print("Assignment complete! Save this file and send it to Jonathan.")
print("God bless, Taylor — great work this week!")
print("=" * 55)