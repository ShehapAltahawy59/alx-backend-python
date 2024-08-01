#!/usr/bin/env python3
def make_multiplier(multiplier :float)->callable[[float],float]:
    def multiplay(x:float)->float:
        return x*multiplier

    return multiplay
