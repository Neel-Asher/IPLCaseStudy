import numpy as np

def generate_scorecards(match_ids, batting_team, total_runs):

    unique_matches = np.unique(match_ids)

    scorecards = {}

    for m in unique_matches:

        mask = match_ids == m

        teams = np.unique(batting_team[mask])

        if len(teams) != 2:
            continue

        t1, t2 = teams

        runs_t1 = np.sum(total_runs[(mask) & (batting_team == t1)])
        runs_t2 = np.sum(total_runs[(mask) & (batting_team == t2)])

        scorecards[m] = {
            t1: runs_t1,
            t2: runs_t2
        }

    return scorecards