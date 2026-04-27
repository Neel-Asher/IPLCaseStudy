import numpy as np
import warnings

import numpy as np

def load_deliveries(path):
    data = np.genfromtxt(
        path,
        delimiter=",",
        dtype=str,
        skip_header=1,
        autostrip=True,
        invalid_raise=False
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

