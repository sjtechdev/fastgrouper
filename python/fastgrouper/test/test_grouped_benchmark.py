import pytest
import pandas as pd
import numpy as np
from   numpy.testing import assert_almost_equal

import fastgrouper.arr
import fastgrouper.li

# Create assymetrical groups
XVALS = np.linspace(500, 1200, 50000)
YVALS = np.linspace(-230, 177.3, 50000)
GIDS  = np.tile(np.arange(500), 100)
GIDS[[14, 19, 230, 87]] = 4
GIDS[[345, 1270, 63, 1287]] = 12

def beepbop(x, y):
    return np.min(np.abs(np.sin(x) + np.sin(y)))

def test_fastgrouper_arr_slice_apply_benchmark(benchmark):
    arr_grpr = fastgrouper.arr.Grouped(GIDS)
    idx = pd.Index(arr_grpr.dedup_gids, name="gids")

    def apply_fn():
        result = arr_grpr.apply(beepbop, XVALS, YVALS)

        # Sorting to make a more fair comparison against pure pandas benchmark
        return pd.Series(result, index=idx).sort_index()

    benchmark(apply_fn)

def test_pure_pandas_slice_apply_benchmark(benchmark):
    df = pd.DataFrame({
        "gids": GIDS,
        "xvals": XVALS,
        "yvals": YVALS
    })
    pdgrpd = df.groupby("gids")

    def apply_fn(r):
        return beepbop(r["xvals"].values, r["yvals"].values)

    benchmark(pdgrpd.apply, apply_fn)

def test_fastgrouper_all_steps_benchmark(benchmark):
    def apply_fn():
        arr_grpr = fastgrouper.arr.Grouped(GIDS)
        idx = pd.Index(arr_grpr.dedup_gids, name="gids")
        result = arr_grpr.apply(beepbop, XVALS, YVALS)

        # Sorting to make a more fair comparison against pure pandas benchmark
        return pd.Series(result, index=idx).sort_index()

    benchmark(apply_fn)

def test_pure_pandas_all_steps_benchmark(benchmark):
    df = pd.DataFrame({
        "gids": GIDS,
        "xvals": XVALS,
        "yvals": YVALS
    })
    pdgrpd = df.groupby("gids")

    def apply_fn():
        return df.groupby("gids").apply(lambda r: beepbop(r["xvals"].values, r["yvals"].values))

    benchmark(apply_fn)
