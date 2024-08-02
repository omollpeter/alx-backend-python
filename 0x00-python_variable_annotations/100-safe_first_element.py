#!/usr/bin/env python3
"""
This module contains the following function:
    safe_first_element - Returns first element of a list None otherwise
"""


from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns first element of an iterable None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
