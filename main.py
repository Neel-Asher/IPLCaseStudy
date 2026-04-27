from src.load_data import load_deliveries, load_matches
import numpy as np

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

match_ids = deliveries[:, 0].astype(int)
overs = deliveries[:, 1].astype(int)
batting_team = deliveries[:, 2]
batter = deliveries[:, 6]
bowler = deliveries[:, 7]
batsman_runs = deliveries[:, 9].astype(int)

batsman_runs = batsman_runs.astype(int)

print("Deliveries shape:", deliveries.shape)
print("Matches shape:", matches.shape)
print("Unique batsman_runs:", np.unique(batsman_runs))
print("Any empty strings in batter:", np.any(batter == ''))
print("Any empty strings in bowler:", np.any(bowler == ''))
print("Over range:", np.min(overs), "to", np.max(overs))