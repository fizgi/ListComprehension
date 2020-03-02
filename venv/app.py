""" A study focuses on list comprehension

    author: Fatih IZGI
    date: 03-Mar-2020
    version: python 3.8.1
"""

from typing import Any, List


def list_copy(lst: List[Any]) -> List[Any]:
    """ Takes a list as a parameter and returns
        a copy of the list using a list comprehension
    """
    copy: List[Any] = [item for item in lst]

    return copy  # return the copied list


def list_intersect(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns
        a new list with the values that are included in both lists
    """
    intersection: List[Any] = [item1 for item1 in lst1 for item2 in lst2 if item1 == item2]

    return intersection
