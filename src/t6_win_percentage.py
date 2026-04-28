import numpy as np

def win_percentage(matches):

    team1 = np.char.strip(matches[:, 7])
    team2 = np.char.strip(matches[:, 8])
    winner = np.char.strip(matches[:, 11])

    teams = np.unique(np.concatenate((team1, team2)))

    matches_played = {team: 0 for team in teams}
    matches_won = {team: 0 for team in teams}

    for i in range(len(matches)):
        t1 = team1[i]
        t2 = team2[i]
        win = winner[i]

        matches_played[t1] += 1
        matches_played[t2] += 1

        if win in matches_won:
            matches_won[win] += 1

    win_percent = {}

    for team in teams:
        if matches_played[team] > 0:
            win_percent[team] = (matches_won[team] / matches_played[team]) * 100
        else:
            win_percent[team] = 0

    return win_percent