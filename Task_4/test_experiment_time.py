from experiment_time import calculate_total_execution_time

def test_overlapping_runs():
    runs = [
        {"experiment_id": "exp1", "start_time": 1, "end_time": 5},
        {"experiment_id": "exp1", "start_time": 3, "end_time": 7},
    ]
    assert calculate_total_execution_time(runs) == {"exp1": 6}


def test_multiple_experiments():
    runs = [
        {"experiment_id": "exp1", "start_time": 1, "end_time": 4},
        {"experiment_id": "exp2", "start_time": 2, "end_time": 6},
        {"experiment_id": "exp1", "start_time": 5, "end_time": 8},
    ]
    assert calculate_total_execution_time(runs) == {
        "exp1": 6,
        "exp2": 4
    }


def test_edge_cases():
    runs = [
        {"experiment_id": "exp1", "start_time": 5, "end_time": 5},  # invalid
        {"experiment_id": "exp1", "start_time": 10, "end_time": 12},
    ]
    assert calculate_total_execution_time(runs) == {"exp1": 2}
