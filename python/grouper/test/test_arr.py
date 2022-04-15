import numpy as np
from   numpy.testing import assert_almost_equal

import grouper.arr
import grouper.li

EXPECTED_APPLY = [3.525, 3.2, -0.3]
EXPECTED_APPLY_EXPAND = [3.525, 3.2 , 3.525, 3.525, -0.3, 3.525, 3.2]
XVALS = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
YVALS = np.array([1.2, 4.2, 8.3, -2.4, -0.8, 5.6, 1.3])
GIDS   = np.array([-23, -24, -23, -23, -25, -23, -24])

def foobar_op(x, y):
    return np.mean(x + y)

def test_arr_grouped():
    
    # Prepare example
    arr_grpr = grouper.arr.Grouped(GIDS)
    
    # Check apply with positional args
    result = arr_grpr.apply(foobar_op, XVALS, YVALS)
    
    # Ensure returned result is a numpy array
    assert isinstance(result, np.ndarray)
    
    # Check values
    assert_almost_equal(result, np.array(EXPECTED_APPLY))
    
    # Check values when using apply with keyword args
    result = arr_grpr.apply(foobar_op, XVALS, y=YVALS)
    assert_almost_equal(result, np.array(EXPECTED_APPLY))
    
    # Check values when using apply_expand
    result = arr_grpr.apply_expand(foobar_op, XVALS, y=YVALS)
    assert_almost_equal(result, np.array(EXPECTED_APPLY_EXPAND))
    
def test_li_grouped():
    
    # Prepare example
    li_grpr = grouper.li.Grouped(GIDS)
    
    # Check apply with keyword args
    result = li_grpr.apply(foobar_op, XVALS, y=YVALS)
    
    # Ensure returned result is a list
    assert isinstance(result, list)
    
    # Check values
    assert_almost_equal(result, EXPECTED_APPLY)