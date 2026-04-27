import numpy as np

def economy_rate(bowler, deliveries):
    
    total_runs = deliveries[:, 9].astype(int) 
    extras_type = deliveries[:, 12]     
    
    unique_bowlers = np.unique(bowler)

    runs_conceded = np.array([
        np.sum(total_runs[bowler == b])
        for b in unique_bowlers
    ])

    valid_balls_mask = extras_type != 'wides'
    valid_bowler = bowler[valid_balls_mask]

    balls_bowled = np.array([
        np.sum(valid_bowler == b)
        for b in unique_bowlers
    ])

    overs = balls_bowled / 6

    economy = runs_conceded / overs

    min_balls = 300
    mask = balls_bowled >= min_balls

    return unique_bowlers[mask], economy[mask]