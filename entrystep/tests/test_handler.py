# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

from unittest import TestCase
from handler import lambda_handler

class HandlerTest(TestCase):

    def test_handler(self):
        event = lambda_handler({}, None)
        self.assertDictEqual(event, {
                'param1': 'param1',
                'param2': 10
            }
        )
