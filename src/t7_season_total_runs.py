import numpy as np

def season_total_runs(matches, deliveries):

    match_ids = deliveries[:, 0].astype(int)
    total_runs = deliveries[:, 11].astype(int)

    match_id_to_season = {
        int(matches[i, 0]): matches[i, 1]
        for i in range(len(matches))
    }

    season_runs = {}

    for i in range(len(deliveries)):
        match_id = match_ids[i]
        run = total_runs[i]

        season = match_id_to_season.get(match_id, None)

        if season is None:
            continue

        if season in season_runs:
            season_runs[season] += run
        else:
            season_runs[season] = run

    return season_runs