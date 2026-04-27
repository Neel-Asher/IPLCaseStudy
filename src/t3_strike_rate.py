import numpy as np

def strike_rate(batter, batsman_runs, deliveries):
    
    extras_type = deliveries[:, 12]
    valid_balls_mask = extras_type != 'wides'

    valid_batter = batter[valid_balls_mask]
    valid_runs = batsman_runs[valid_balls_mask]

    unique_batters = np.unique(valid_batter)

    total_runs = np.array([
        np.sum(valid_runs[valid_batter == b])
        for b in unique_batters
    ])

    balls_faced = np.array([
        np.sum(valid_batter == b)
        for b in unique_batters
    ])

    strike_rates = (total_runs / balls_faced) * 100
    
    min_balls = 100

    mask = balls_faced >= min_balls

    filtered_batters = unique_batters[mask]
    filtered_sr = strike_rates[mask]

    return filtered_batters, filtered_sr