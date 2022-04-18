[![<sjoshistrats>](https://circleci.com/gh/sjoshistrats/fastgrouper.svg?style=shield)](https://app.circleci.com/pipelines/github/sjoshistrats/fastgrouper?branch=master)

# fastgrouper
Fast groupby-apply operations in python.
  
# Install
  
Users can install the package from PyPI via:
  
```shell
python -m pip install fastgrouper
```

# Usage

Use the `arr` interface, for numpy array related applications.

```python
import numpy as np
import fastgrouper.arr
  
def baz(x, y):
    return np.mean(x + y) - 3

# Sample arrays, to slice
xvals = np.array([1, 2, 10])
yvals = np.array([4, 5, 6])
  
# Group ids
gids  = np.array([1, -3, 1])

# Perform groupby-apply; note that keyword args are supported as well.
grpd = fastgrouper.arr.Grouped(gids)
result = grpd.apply(baz, xvals, y=yvals) # np.array([7.5, 4])

# The gids correponding to the result above can be found via the `dedup_gids` attribute.
grpd.dedup_gids # np.array([ 1, -3])

# Users can also perform groupby-apply, and then expand results back to align with the original gids.
result = grpd.apply_expand(baz, xvals, yvals) # np.array([7.5, 4, 7.5])
```

The `li` interface returns the results over the groups as a list (instead of an array); this may be useful for functions that return different-sized results. Note that in all interfaces (e.g. both `arr` and `li`), the order of the group elements is preserved when the group slices are passed to the function being applied.

  
```python
import numpy as np
import fastgrouper.li
  
def bop(x):
    return list(x)

# Sample arrays, to slice
xvals = np.array([2, 3, 4])
  
# Group ids
gids  = np.array([10, -20, 10])

grpd = fastgrouper.li.Grouped(gids)
grpd.apply(bop, xvals) # [[2, 4], [3]]
```
  
For additional examples, checkout the [tests](./python/fastgrouper/test).
  
# Benchmarks

Checkout the benchmarks [here](./python/fastgrouper/test/test_grouped_benchmark.py) for a sample comparison between the `pandas` groupby-apply and `fastgrouper` groupby-apply workflows. While it is difficult to compare the two perfectly, I tried to make the comparison as fair as possible.

Results from running the benchmarks on a sample machine with an Intel(R) Core(TM) i7-4870HQ CPU @ 2.50GHz:
  
```console
---------------------------------------------------------------------------------------------- benchmark: 4 tests ---------------------------------------------------------------------------------------------
Name (time in ms)                                  Min                Max               Mean            StdDev             Median               IQR            Outliers       OPS            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fastgrouper_arr_slice_apply_benchmark      5.8296 (1.0)       6.6786 (1.0)       6.0080 (1.0)      0.1165 (1.0)       6.0071 (1.0)      0.1294 (1.0)          35;5  166.4435 (1.0)         147           1
test_fastgrouper_all_steps_benchmark            7.7704 (1.33)     10.3270 (1.55)      8.0946 (1.35)     0.3171 (2.72)      8.0872 (1.35)     0.2511 (1.94)          6;2  123.5386 (0.74)        121           1
test_pure_pandas_slice_apply_benchmark         42.4697 (7.29)     46.9096 (7.02)     43.0534 (7.17)     0.9816 (8.42)     42.6915 (7.11)     0.4361 (3.37)          2;3   23.2270 (0.14)         22           1
test_pure_pandas_all_steps_benchmark           43.4275 (7.45)     45.2340 (6.77)     43.8837 (7.30)     0.4243 (3.64)     43.7748 (7.29)     0.4973 (3.84)          3;1   22.7875 (0.14)         23           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

