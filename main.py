from src.load_data import load_deliveries, load_matches
from src.schema import DELIVERY_COLS, MATCH_COLS
from src.t1_total_runs import total_runs_per_match
from src.t2_top_batters import top_5_batters
from src.t3_strike_rate import strike_rate
from src.t4_economy import economy_rate
from src.t5_runs_per_over import runs_per_over
from src.t6_win_percentage import win_percentage
from src.t7_season_total_runs import season_total_runs
from src.t8_highest_scoring_match import highest_scoring_match
from src.t9_match_winner import match_winner
from src.t10_toss_impact import toss_impact
import numpy as np

deliveries = load_deliveries("data/deliveries.csv")
matches = load_matches("data/matches.csv")

match_ids = deliveries[:, DELIVERY_COLS["match_id"]].astype(int)
overs = deliveries[:, DELIVERY_COLS["over"]].astype(int)
batting_team = deliveries[:, DELIVERY_COLS["batting_team"]]
batter = deliveries[:, DELIVERY_COLS["batter"]]
bowler = deliveries[:, DELIVERY_COLS["bowler"]]

batsman_runs = deliveries[:, DELIVERY_COLS["batsman_runs"]].astype(int)
total_runs_col = deliveries[:, DELIVERY_COLS["total_runs"]].astype(int)

match_ids = deliveries[:, DELIVERY_COLS["match_id"]].astype(int)
total_runs_col = deliveries[:, DELIVERY_COLS["total_runs"]].astype(int)

batter = deliveries[:, DELIVERY_COLS["batter"]]
bowler = deliveries[:, DELIVERY_COLS["bowler"]]

batsman_runs = deliveries[:, DELIVERY_COLS["batsman_runs"]].astype(int)
total_runs_col = deliveries[:, DELIVERY_COLS["total_runs"]].astype(int)

unique_matches, match_totals = total_runs_per_match(match_ids, total_runs_col)
top_batters_list, runs = top_5_batters(batter, batsman_runs)
batters_sr, sr = strike_rate(batter, batsman_runs, deliveries)
bowlers, eco = economy_rate(bowler, deliveries)
avg_runs = runs_per_over(overs, total_runs_col)
team_win_pct = win_percentage(matches)
sorted_teams = sorted(team_win_pct.items(), key=lambda x: x[1], reverse=True)

match_season_map = {}

for i in range(len(matches)):
    match_id = int(matches[i][0])
    season = matches[i][1]
    match_season_map[match_id] = season

season_runs_map = {}

for i in range(len(deliveries)):
    match_id = int(deliveries[i][0])
    runs = int(deliveries[i][10])

    season = match_season_map.get(match_id)
    
    if season is None:
        continue

    if season not in season_runs_map:
        season_runs_map[season] = 0   

    season_runs_map[season] += runs

sorted_seasons = sorted(season_runs_map.items())
highest_match_id, highest_runs = highest_scoring_match(match_ids, total_runs_col)
match_winners = match_winner(match_ids, batting_team, total_runs_col)
toss_wins, total = toss_impact(matches, match_ids, batting_team, total_runs_col)

print("\nToss Impact Analysis:")
print(f"Toss winner scored more in {toss_wins} out of {total} matches")
print(f"Percentage: {round((toss_wins/total)*100, 2)}%")