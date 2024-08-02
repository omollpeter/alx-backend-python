#!/usr/bin/env python3
"""
This module contains the following function:
    zoom_array: Enlarges elements of a list by a factor
"""


from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns array with enlarged elements by a factor
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
