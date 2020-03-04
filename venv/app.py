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

    return intersection  # return the intersection list

def list_difference(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns
        a new list with the values in list1 that are not included in list2
    """
    difference: List[Any] = [item for item in lst1 if item not in lst2]

    return difference  # return the difference

def remove_vowels(string: str) -> str:
    """ a function that given a string, splits the string on whitespace into words
        and returns a new string that includes only the words that do NOT begin with vowels
    """
    # join each word separated by " " after removing the words which do not begin with vowels
    new_string: str = ' '.join([word for word in string.split(" ")
                                if not word.lower().startswith(('a', 'e', 'i', 'o', 'u'))])

    return new_string

def check_pwd(password: str) -> bool:
    """ a function that takes a string as a parameter,
        checks the string if it is a valid password
        and returns a boolean value.
    """
    lower_count: int = 0
    upper_count: int = 0
    start_digit: bool = False

    if password[0].isdigit():  # should start with a digit
        start_digit = True

        # then count the lowercase and uppercase letters
        lower_count: int = sum([i/i for i, char in enumerate(password) if char.islower()])
        upper_count: int = sum([i/i for i, char in enumerate(password) if char.isupper()])

    # return True when all conditions are met
    return start_digit and lower_count >= 1 and upper_count >= 2
