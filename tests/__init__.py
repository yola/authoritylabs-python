# -*- coding: utf-8 -*-

import inspect

from demands import HTTPServiceClient, HTTPServiceError
from mock import Mock, patch
from requests import Session, Response
import unittest2


class PatchedSessionTests(unittest2.TestCase):
    def setUp(self):
        # must patch inspect since it is used on Session.request, and when
        # Session.request is mocked, inspect blows up
        self.request_args = inspect.getargspec(Session.request)
        self.inspect_patcher = patch('demands.inspect.getargspec')
        self.patched_inspect = self.inspect_patcher.start()
        self.patched_inspect.return_value = self.request_args

        self.request_patcher = patch.object(Session, 'request')
        self.request = self.request_patcher.start()
        self.response = Mock(spec=Response(), status_code=200)
        self.request.return_value = self.response

    def tearDown(self):
        self.request_patcher.stop()
        self.inspect_patcher.stop()
