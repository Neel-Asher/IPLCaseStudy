import numpy as np
import warnings

def load_deliveries(path):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        data = np.genfromtxt(
            path,
            delimiter=",",
            dtype=str,
            skip_header=1,
            autostrip=True,
            invalid_raise=False
        )

    # remove empty rows only
    data = np.array([row for row in data if len(row) == 17])

    return data


def load_matches(path):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        data = np.genfromtxt(
            path,
            delimiter=",",
            dtype=str,
            skip_header=1,
            autostrip=True,
            invalid_raise=False
        )

    data = np.array([row for row in data if len(row) == 20])

    return data