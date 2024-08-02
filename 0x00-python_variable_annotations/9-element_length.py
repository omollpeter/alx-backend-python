#!/usr/bin/env python3
"""
This module contains the following function:
    element_length - Returns the length of each iterable in a list
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple each iterable with its length in a list
    """
    return [(i, len(i)) for i in lst]
