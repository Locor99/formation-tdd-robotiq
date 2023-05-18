import unittest

from src.chap1_functions.pack_unpack import *

class MyTestCase(unittest.TestCase):

    def test_sum_SHOULD_be_correct_AND_not_use_len(self):
        a,b,c,d = 1,2,3,4
        sent = a,b,c,d

        received = unpack_and_repack_all_four_arguments_in_reverse_order(sent)
        r1, r2, r3, r4 = received

        self.assertEqual(r4, a)
        self.assertEqual(r3, b)
        self.assertEqual(r2, c)
        self.assertEqual(r1, d)
