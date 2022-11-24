"""
Sample tests
"""

from django.test import SimpleTestCase

from unittest.mock import patch

from app import calc


class CalcTest(SimpleTestCase):
    ''' Test the calc module '''

    def test_add_numbers(self):
        ''' Test adding 2 numbers '''
        self.assertEqual(calc.add(3, 8), 11)

    def test_sub_numbers(self):
        self.assertEqual(calc.sub(5, 11), -6)
