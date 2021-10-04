import unittest
from .package1 import array


class TestArray(unittest.TestCase):
    def test_sum(self):
        result = array.Array().sum(6, '1 2 3 4 5 6')
        self.assertEqual(result, 21)

    def test_sum_raise_exception(self):
        self.assertRaises(Exception, lambda: array.Array().sum(5, '1 2 3 4 10 11'))


"""
UnitTest Method

assertEqual(a, b)	            a == b	
assertNotEqual(a, b)	        a != b	
assertTrue(x)	                bool(x) is True	
assertFalse(x)	                bool(x) is False	
assertIs(a, b)	                a is b	
assertIsNot(a, b)	            a is not b	
assertIsNone(x)	                x is None	
assertIsNotNone(x)  	        x is not None	
assertIn(a, b)              	a in b	
assertNotIn(a, b)   	        a not in b	
assertIsInstance(a, b)	        isinstance(a, b)	
assertNotIsInstance(a, b)	    not isinstance(a, b)	
"""