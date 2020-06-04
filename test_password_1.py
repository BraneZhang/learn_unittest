#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


class PasswordTestCase(unittest.TestCase):

    def setUp(self):
        print('set up')
        self.test_data = [
            dict(name='jack', password='Iloverose'),
            dict(name='rose', password='Ilovejack'),
            dict(name='tom', password='password123'),
            dict(name='jerry', password='password'),
        ]

    def test_weak_password(self):
        for data in self.test_data:
            passwd = data['password']

            self.assertTrue(len(passwd) >= 6)

            msg = "user %s has a weak password" % (data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'password123', msg)

    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()
