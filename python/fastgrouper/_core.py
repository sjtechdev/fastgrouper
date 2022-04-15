import numpy as np
import pandas as pd

def _split(x, y):
    return np.split(x, y)[:-1]

def _build_arr_idcs(index):
    srt = np.argsort(index, kind="stable")
    uni = np.bincount(index)
    csum = np.cumsum(uni)
    final = _split(srt, csum)
    return final

def apply(arr_idcs, fn, *args, **kwargs):
    return [
        fn( 
            *( a[arr_idc] for a in args ), 
            **{ k: v[arr_idc] for k, v in kwargs.items() }
        )
        for arr_idc in arr_idcs
    ]

def apply_expand(take_idcs, arr_idcs, fn, *args, **kwargs):
    result = np.array(apply(arr_idcs, fn, *args, **kwargs))
    return result[take_idcs]

def construct_grouper_components(gids):
    inversion_idcs, dedup_gids = pd.factorize(gids)
    arr_idcs = _build_arr_idcs(inversion_idcs)
    return inversion_idcs, dedup_gids, arr_idcs