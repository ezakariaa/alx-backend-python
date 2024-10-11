#!/usr/bin/env python3
""" string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments
    """

    return (k, v**2)
