from typing import *

def min_indval(iterator: Iterable) -> Tuple[int, Any]:
    min_ind: int = 0
    min_val: Any = None
    for ind, val in enumerate(iterator):
        if val < min_val:
            min_ind = ind
            min_val = val
    return min_ind, min_val
