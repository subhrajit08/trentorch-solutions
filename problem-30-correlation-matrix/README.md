# Correlation Matrix

Intermediate | problemset | data-stats-for-ds | eda

Compute the matrix of pairwise Pearson correlations between the columns of a data matrix.

Implement `solve(X)`.

**Returns.** Return a symmetric $d\times d$ NumPy array with ones on the diagonal. A constant column has no variance, so its correlations are `nan`.

### Examples

**Example 1**

Input:

```python
solve([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
```

Output:

```text
[[1.0, 1.0], [1.0, 1.0]]
```

**Example 2**

Input:

```python
solve([[1.0, 3.0], [2.0, 2.0], [3.0, 1.0]])
```

Output:

```text
[[1.0, -1.0], [-1.0, 1.0]]
```
