from collections import defaultdict

def calculate_total_execution_time(runs):
    """
    Calculate total execution time per experiment,
    accounting for overlapping runs.
    """
    if not runs:
        return {}

    experiments = defaultdict(list)

    # Group runs by experiment_id
    for run in runs:
        exp_id = run["experiment_id"]
        start = run["start_time"]
        end = run["end_time"]

        if start >= end:
            continue  # ignore invalid runs

        experiments[exp_id].append((start, end))

    result = {}

    # Process each experiment separately
    for exp_id, intervals in experiments.items():
        # Sort by start time
        intervals.sort()

        total_time = 0
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= current_end:
                # Overlapping run → extend end if needed
                current_end = max(current_end, end)
            else:
                # No overlap → finalize previous interval
                total_time += current_end - current_start
                current_start, current_end = start, end

        # Add last interval
        total_time += current_end - current_start

        result[exp_id] = total_time

    return result
