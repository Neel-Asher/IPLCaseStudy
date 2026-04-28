import numpy as np

def highest_scoring_match(match_ids, runs):

    unique_matches = np.unique(match_ids)

    max_runs = 0
    max_match = None

    for m in unique_matches:
        total = np.sum(runs[match_ids == m])

        if total > max_runs:
            max_runs = total
            max_match = m

    return max_match, max_runs