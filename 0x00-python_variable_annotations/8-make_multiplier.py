#!/usr/bin/env python3
"""
This module contains the following function:
    make_multiplier - Takes a float and returns a function that multip
                        lies float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """
    def multiplier_func(value: float) -> float:
        """
        Returns product of float and float
        """
        return value * multiplier
    return multiplier_func
