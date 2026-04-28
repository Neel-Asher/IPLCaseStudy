from src.load_data import load_deliveries, load_matches
from src.t1_total_runs import total_runs_per_match
from src.t2_top_batters import top_5_batters
from src.t3_strike_rate import strike_rate
from src.t4_economy import economy_rate
from src.t5_runs_per_over import runs_per_over
from src.t6_win_percentage import win_percentage
from src.t7_season_total_runs import season_total_runs
import numpy as np

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

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

unique_matches, match_totals = total_runs_per_match(match_ids, total_runs_col)
top_batters_list, runs = top_5_batters(batter, batsman_runs)
batters_sr, sr = strike_rate(batter, batsman_runs, deliveries)
bowlers, eco = economy_rate(bowler, deliveries)
avg_runs = runs_per_over(overs, total_runs_col)
team_win_pct = win_percentage(matches)
sorted_teams = sorted(team_win_pct.items(), key=lambda x: x[1], reverse=True)

seasons = matches[:, 1]
season_runs = season_total_runs(matches, deliveries)

print("\nSeason-wise Total Runs:")

sorted_seasons = sorted(season_runs.items())

for season, runs in sorted_seasons:
    print(f"{season}: {runs}")