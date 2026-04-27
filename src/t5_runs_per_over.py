import numpy as np

def runs_per_over(over, total_runs):

    overs = np.arange(1, 21)

    total = np.array([
        np.sum(total_runs[over == o]) for o in overs
    ])

    balls = np.array([
        np.sum(over == o) for o in overs
    ])

    avg_runs = np.zeros(20)

    valid = balls > 0
    avg_runs[valid] = total[valid] / (balls[valid] / 6)

    return avg_runs