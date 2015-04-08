from time import sleep

import unittest2

from authoritylabs.utils import memoized_ttl


class MemoizedTTLTestCase(unittest2.TestCase):
    def setUp(self):
        self.num = 1

    def return_num(self):
        return self.num

    def test_no_ttl(self):
        memoized_func = memoized_ttl()(self.return_num)
        old_num = memoized_func()
        self.num = 5
        sleep(5)
        new_num = memoized_func()
        self.assertEqual(old_num, new_num)

    def test_expired_ttl(self):
        memoized_func = memoized_ttl(4)(self.return_num)
        old_num = memoized_func()
        self.num = 2
        sleep(5)
        new_num = memoized_func()
        self.assertNotEqual(old_num, new_num)

    def test_valid_ttl(self):
        memoized_func = memoized_ttl(4)(self.return_num)
        old_num = memoized_func()
        self.num = 2
        sleep(5)
        new_num = memoized_func()
        self.assertEqual(old_num, 1)
        self.assertEqual(new_num, 2)
