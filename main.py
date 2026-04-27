from src.load_data import load_deliveries, load_matches
from src.t1_total_runs import total_runs_per_match

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

match_ids = deliveries[:, 0].astype(int)
overs = deliveries[:, 1].astype(int)
batting_team = deliveries[:, 2]
batter = deliveries[:, 6]
bowler = deliveries[:, 7]
batsman_runs = deliveries[:, 9].astype(int)

unique_matches, total_runs = total_runs_per_match(match_ids, batsman_runs)

for i in range(5):
    print(unique_matches[i], total_runs[i])