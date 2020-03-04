""" Test implementation class of the study
    which focuses on string methods, slices,
    working with files, and automated testing

    author: Fatih IZGI
    date: 21-Feb-2020
    version: python 3.8.1
"""

import unittest

from app import list_copy, list_intersect, list_difference, remove_vowels, check_pwd
from app import DonutQueue


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
        self.assertTrue(list_intersect([1, 2, 3], [1, 2, 3]) == [1, 2, 3])

    def test_list_difference(self):
        """ testing list difference """
        self.assertTrue(list_difference([1, 2, 3], [1, 2, 4]) == [3])
        self.assertTrue(list_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3])
        self.assertTrue(list_difference([1, 2, 3], [1, 2, 3]) == [])

    def test_remove_vowels(self):
        """ testing remove vowels """
        self.assertTrue(remove_vowels("Amy is my favorite daughter") == "my favorite daughter")
        self.assertTrue(remove_vowels('Jan is my best friend') == "Jan my best friend")
        self.assertTrue(remove_vowels('This is a test string') == "This test string")
        self.assertTrue(remove_vowels('And and Ever ever in In or Or url Url') == "")

    def test_check_pwd(self):
        """ testing check password """
        self.assertTrue(check_pwd("1ASd"))
        self.assertTrue(check_pwd("223dddAS"))
        self.assertFalse(check_pwd("1aaS"))
        self.assertFalse(check_pwd("aSS1"))


class DonutQueueTest(unittest.TestCase):
    """ Test class of the DonutQueue class """
    def test_queue(self):
        """ testing queue """
        dq = DonutQueue()
        self.assertIsNone(dq.next_customer())
        dq.arrive("Sujit", False)
        dq.arrive("Fei", False)
        dq.arrive("Prof JR", True)
        self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
        dq.arrive("Nanda", True)
        self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(dq.next_customer(), "Prof JR")
        self.assertEqual(dq.next_customer(), "Nanda")
        self.assertEqual(dq.next_customer(), "Sujit")
        self.assertEqual(dq.waiting(), "Fei")
        self.assertEqual(dq.next_customer(), "Fei")
        self.assertIsNone(dq.next_customer())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
