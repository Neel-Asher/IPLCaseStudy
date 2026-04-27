import numpy as np

def total_runs_per_match(match_ids, batsman_runs):
    unique_matches = np.unique(match_ids)

    total_runs = np.array([
        np.sum(batsman_runs[match_ids == match])
        for match in unique_matches
    ])

    return unique_matches, total_runs