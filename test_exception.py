#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


class DivZeroTestCase(unittest.TestCase):

    def test_should_raise_exception(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
            # 2 / 3


if __name__ == '__main__':
    unittest.main()
