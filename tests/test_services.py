#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_services
----------------------------------

Tests for `authoritylabs.services` module.
"""

import unittest2

from authoritylabs.services import AuthorityLabsPartnerApi


class TestPartnerApi(unittest2.TestCase):
    def setUp(self):
        self.client = AuthorityLabsPartnerApi(
            api_key='test_key', account_id='test_id')

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest2.main()
