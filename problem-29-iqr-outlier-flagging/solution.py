import numpy as np


def solve(x):
    """Implement IQR Outlier Flagging from the mathematical contract in README.md."""
    x = np.asarray(x, float)
    q1 = np.quantile(x, 0.25)
    q3 = np.quantile(x, 0.75)
    iqr = q3 - q1
    return (x < q1-1.5*iqr) | (x > q3+1.5*iqr)
