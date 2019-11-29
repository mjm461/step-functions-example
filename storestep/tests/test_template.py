# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os

from unittest import TestCase, mock
from storestep import StoreStep


class HandlerTest(TestCase):

    @mock.patch.dict(os.environ, {'PARAM_STR': 'string', 'PARAM_INT': '1'})
    def test_handler(self) -> None:
        event = StoreStep().handler(
            {},
            None
        )
        self.assertDictEqual({}, event)
