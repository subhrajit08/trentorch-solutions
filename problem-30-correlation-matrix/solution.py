import numpy as np


def solve(x):
    # TODO: Return the Pearson correlation matrix between columns of X.
    x = np.asarray(x, dtype=float)
    return np.corrcoef(x, rowvar=False)
