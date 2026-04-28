import numpy as np

def match_winner(match_ids, batting_team, total_runs):

    unique_matches = np.unique(match_ids)

    results = {}

    for m in unique_matches:

        mask = match_ids == m

        teams = np.unique(batting_team[mask])

        if len(teams) != 2:
            continue

        team1, team2 = teams

        runs_team1 = np.sum(total_runs[(mask) & (batting_team == team1)])
        runs_team2 = np.sum(total_runs[(mask) & (batting_team == team2)])

        if runs_team1 > runs_team2:
            winner = team1
        elif runs_team2 > runs_team1:
            winner = team2
        else:
            winner = "Tie"

        results[m] = winner

    return results