#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple,Any,Union
# The types of the elements of the input are not know
def safe_first_element(lst:Sequence)->Union[Any,None]:
    if lst:
        return lst[0]
    else:
        return None
