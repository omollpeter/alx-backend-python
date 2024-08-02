#!/usr/bin/env python3
"""
This module contains the following function:
    safely_get_value - Returns a value from a dict using key
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar("T")


def safely_get_value(
        dct: Mapping, key: Any, default : Union[T, None] = None
    ) -> Union[Any, T]:
    """
    Returns a value from a dict using key
    """
    if key in dct:
        return dct[key]
    else:
        return default
