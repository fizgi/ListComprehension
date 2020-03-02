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
    intersection: List[Any] = [item for item in lst1 if item in lst2]

    return intersection

def list_difference(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns
        a new list with the values in list1 that are not included in list2
    """
    difference: List[Any] = [item for item in lst1 if item not in lst2]

    return difference

def remove_vowels(string: str) -> str:
    """ a function that given a string, splits the string on whitespace into words
        and returns a new string that includes only the words that do NOT begin with vowels
    """
    new_string: str = ' '.join([word for word in string.split(" ")
                                if not word.lower().startswith(('a', 'e', 'i', 'o', 'u'))])

    return new_string
