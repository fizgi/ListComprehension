""" Test implementation class of the study
    which focuses on string methods, slices,
    working with files, and automated testing

    author: Fatih IZGI
    date: 21-Feb-2020
    version: python 3.8.1
"""

import unittest
from app import list_copy, list_intersect


class ListTest(unittest.TestCase):
    """ Test class of the methods """
    def test_list_copy(self):
        """ testing list copy """
        self.assertTrue([1, 2, 3, 4, 5] == list_copy([1, 2, 3, 4, 5]))
        self.assertTrue(list("a string to test") == list_copy("a string to test"))

    def test_list_intersect(self):
        """ testing list intersect """
        self.assertTrue(list_intersect([1, 2, 3], [1, 2, 4]) == [1, 2])
        self.assertTrue(list_intersect([1, 2, 3], [4, 5, 6]) == [])



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
