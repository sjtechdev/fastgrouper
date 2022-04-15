import numpy as np

from   ._core import (
    apply,
    apply_expand, 
    construct_grouper_components
)

class Grouped():
    
    def __init__(self, gids):
        self.inversion_idcs, self.dedup_gids, self.arr_idcs = construct_grouper_components(gids)
        
    def apply(self, fn, *args, **kwargs):
        return np.array(apply(self.arr_idcs, fn, *args, **kwargs))
    
    def apply_expand(self, fn, *args, **kwargs):
        return apply_expand(self.inversion_idcs, self.arr_idcs, fn, *args, **kwargs)