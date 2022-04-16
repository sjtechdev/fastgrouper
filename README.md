[![<sjoshistrats>](https://circleci.com/gh/sjoshistrats/fastgrouper.svg?style=shield)](https://app.circleci.com/pipelines/github/sjoshistrats/fastgrouper?branch=master)

# fastgrouper
Allows for fast groupby-apply operations, in python.
  
# Install
  
Users can install the package from PyPI via:
  
```shell
python -m pip install fastgrouper
```

# Usage

Use the `arr` interface, for numpy array focused applications.

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

The `li` interface returns the results over the groups as a list (instead of an array); this may be useful for functions that return different-sized results. Note that in all interfaces (e.g. both `arr` and `li`), the order in which the group elements appear is preserved when the group slices are passed to the function being applied.

  
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
