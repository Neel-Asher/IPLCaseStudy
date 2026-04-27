import numpy as np
import warnings

def load_deliveries(path):
    data = np.genfromtxt(
        path,
        delimiter=",",
        skip_header=1,
        dtype=str,
        encoding="utf-8"
    )
    return data


def load_matches(path):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        data = np.genfromtxt(
            path, 
            delimiter=",",
            skip_header=1,
            dtype=str,
            encoding="utf-8",
            invalid_raise=False
        )
    return data

