import numpy as np

def toss_impact(matches, match_ids, batting_team, total_runs):

    toss_map = {}

    for row in matches:
        try:
            match_id = int(row[0])
            toss_winner = row[9]
            toss_map[match_id] = toss_winner
        except:
            continue

    unique_matches = np.unique(match_ids)

    toss_winner_scored_more = 0
    total_matches = 0

    for m in unique_matches:

        if m not in toss_map:
            continue

        mask = match_ids == m
        teams = np.unique(batting_team[mask])

        if len(teams) != 2:
            continue

        t1, t2 = teams

        runs_t1 = np.sum(total_runs[(mask) & (batting_team == t1)])
        runs_t2 = np.sum(total_runs[(mask) & (batting_team == t2)])

        toss_winner = toss_map[m]

        if toss_winner not in teams:
            continue

        total_matches += 1

        if toss_winner == t1 and runs_t1 > runs_t2:
            toss_winner_scored_more += 1
        elif toss_winner == t2 and runs_t2 > runs_t1:
            toss_winner_scored_more += 1

    return toss_winner_scored_more, total_matches