from   ._core import (
    apply, 
    construct_grouper_components
)

class Grouped():
    
    def __init__(self, gids):
        self.inversion_idcs, self.dedup_gids, self.arr_idcs = construct_grouper_components(gids)
        
    def apply(self, fn, *args, **kwargs):
        return apply(self.arr_idcs, fn, *args, **kwargs)