#!/usr/bin/env python3
"""
This module contains the following function:
    to_kv - Takes a string and int/float and returns a tuple
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of the arguments
    """
    return k, v
