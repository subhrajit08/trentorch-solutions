import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    x = np.asarray(x, dtype=float)
    s = np.max(np.abs(x))
    if s == 0:
        return 0.0
    return float(s * np.sqrt(np.sum((x / s)**2)))
