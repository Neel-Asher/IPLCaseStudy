from src.load_data import load_deliveries, load_matches
from src.t1_total_runs import total_runs_per_match
from src.t2_top_batters import top_5_batters
from src.t3_strike_rate import strike_rate
from src.t4_economy import economy_rate
from src.t5_runs_per_over import runs_per_over
import numpy as np

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

print("Shape:", deliveries.shape)

match_ids = deliveries[:, 0].astype(int)
overs = deliveries[:, 4].astype(int) 
batting_team = deliveries[:, 2]
batter = deliveries[:, 6]
bowler = deliveries[:, 7]
batsman_runs = deliveries[:, 9].astype(int)
total_runs_col = deliveries[:, 11].astype(int)

valid_mask = (overs >= 1) & (overs <= 20)

deliveries = deliveries[valid_mask]

match_ids = deliveries[:, 0].astype(int)
overs = deliveries[:, 4].astype(int)
batter = deliveries[:, 6]
bowler = deliveries[:, 7]
batsman_runs = deliveries[:, 9].astype(int)
total_runs_col = deliveries[:, 11].astype(int)

print("Unique overs:", np.unique(overs))

unique_matches, match_totals = total_runs_per_match(match_ids, total_runs_col)
top_batters_list, runs = top_5_batters(batter, batsman_runs)
batters_sr, sr = strike_rate(batter, batsman_runs, deliveries)
bowlers, eco = economy_rate(bowler, deliveries)
avg_runs = runs_per_over(overs, total_runs_col)

print("\nAverage Runs per Over:")
for i in range(20):
    if avg_runs[i] == 0:
        print(f"Over {i+1}: No data")
    else:
        print(f"Over {i+1}: {round(avg_runs[i], 2)}")