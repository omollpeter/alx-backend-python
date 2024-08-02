#!/usr/bin/env python3
"""
This module contains the following function:
    sum_mixed_list - Returns sum of elements(int, float) in a list
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns sum of elements(int, float) in a list
    """
    return sum(mxd_list)
