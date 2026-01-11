# Task 4 – Experiment Execution Time

## Problem
Given multiple experiment runs with start and end times,
calculate total execution time per experiment without double-counting overlaps.

## Approach
1. Group runs by experiment_id
2. Sort runs by start_time
3. Merge overlapping intervals
4. Sum merged durations

## Edge Cases Handled
- Empty input
- Invalid runs (start_time >= end_time)
- Multiple experiments
- Fully overlapping runs

## Time Complexity
Let N be the number of runs.

- Grouping: O(N)
- Sorting per experiment: O(N log N)
- Merging intervals: O(N)

Overall Time Complexity: **O(N log N)**  
Space Complexity: **O(N)**

## How to Run Tests
```bash
python test_experiment_time.py
