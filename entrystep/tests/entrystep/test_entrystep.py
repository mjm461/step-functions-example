# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os

from unittest import TestCase, mock
from entrystep import EntryStep


class HandlerTest(TestCase):

    @mock.patch.dict(os.environ, {'MIN_CHARS': '2', 'MAX_CHARS': '2'})
    def test_handler(self) -> None:
        event = EntryStep().handler(
            {},
            None
        )
        self.assertEqual(2, len(event['prefix']))
