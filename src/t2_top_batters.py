import numpy as np

def top_5_batters(batter, batsman_runs):
    unique_batters = np.unique(batter)

    total_runs = np.array([
        np.sum(batsman_runs[batter == b])
        for b in unique_batters
    ])

    sorted_indices = np.argsort(total_runs)[::-1]

    top5_indices = sorted_indices[:5]

    return unique_batters[top5_indices], total_runs[top5_indices]