from src.load_data import load_deliveries, load_matches
from src.t1_total_runs import total_runs_per_match
from src.t2_top_batters import top_5_batters
from src.t3_strike_rate import strike_rate
from src.t4_economy import economy_rate
import numpy as np

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

match_ids = deliveries[:, 0].astype(int)
overs = deliveries[:, 1].astype(int)
batting_team = deliveries[:, 2]
batter = deliveries[:, 6]
bowler = deliveries[:, 7]
batsman_runs = deliveries[:, 9].astype(int)
total_runs_col = deliveries[:, 11].astype(int)
top_batters, runs = top_5_batters(batter, batsman_runs)
batters_sr, sr = strike_rate(batter, batsman_runs, deliveries)
bowlers, eco = economy_rate(bowler, deliveries)

unique_matches, match_totals = total_runs_per_match(match_ids, total_runs_col)

print("\nTop 5 Economical Bowlers:")

sorted_idx = np.argsort(eco)  # ascending (lower is better)

for i in range(5):
    idx = sorted_idx[i]
    print(bowlers[idx], round(eco[idx], 2))