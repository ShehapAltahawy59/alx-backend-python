from typing import Iterable, Sequence, List, Tuple,Any,Union,TypeVar

T = TypeVar("T")
def safely_get_value(dct:map, key, default:Union[~T,None] = None)->Union[Any,~T]:
    if key in dct:
        return dct[key]
    else:
        return default
