# IQR Outlier Flagging

Intermediate | problemset | data-stats-for-ds | eda

Flag observations that lie more than $1.5$ interquartile ranges below the first quartile or above the third quartile (Tukey's fences).

Implement `solve(x)`.

**Returns.** Return a boolean NumPy array, `True` where a value is an outlier.

### Examples

**Example 1**

Input:

```python
solve([1.0, 2.0, 3.0, 4.0, 100.0])
```

Output:

```text
[False, False, False, False, True]
```

**Example 2**

Input:

```python
solve([1.0, 2.0, 3.0])
```

Output:

```text
[False, False, False]
```
