""" A study focuses on list comprehension

    author: Fatih IZGI
    date: 03-Mar-2020
    version: python 3.8.1
"""

from typing import Any, List, Optional


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


class DonutQueue:
    """ a class that tracks customers as they arrive at the donut shop
    """
    def __init__(self) -> None:
        """ store two queues for ordinary and vip
        """
        self.queue = list()
        self.queue_vip = list()

    def arrive(self, name: str, vip: bool) -> None:
        """ insert new customer to the related queue
        """
        if vip is True:
            self.queue_vip.insert(0, name)
        else:
            self.queue.insert(0, name)

    def next_customer(self) -> Optional[str]:
        """ return the next customer (pop from the queue)
        """
        if len(self.queue_vip) == 0 and len(self.queue) == 0:
            return None  # retun None if no one in the queues

        # return next customer, vip first
        return self.queue_vip.pop() if len(self.queue_vip) > 0 else self.queue.pop()

    def waiting(self) -> Optional[str]:
        """ retun the waiting queue by combining ordinary and vip queues
        """
        queue_list: List[str] = []  # to store combined queue

        for vip in self.queue_vip[::-1]:  # vip first
            queue_list.append(vip)
        for person in self.queue[::-1]:  # then ordinary
            queue_list.append(person)

        final_queue: str = ", ".join(queue_list)  # list to string

        return final_queue  # return the queue
