from src.load_data import load_deliveries, load_matches
from src.t1_total_runs import total_runs_per_match
from src.t2_top_batters import top_5_batters

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

unique_matches, match_totals = total_runs_per_match(match_ids, total_runs_col)

print("\nTop 5 Batters:")
for i in range(5):
    print(top_batters[i], runs[i])