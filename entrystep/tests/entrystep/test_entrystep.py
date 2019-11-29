# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os

from unittest import TestCase, mock
from entrystep import EntryStep


class HandlerTest(TestCase):

    @mock.patch.dict(os.environ, {'MIN_CHARS': '2', 'MAX_CHARS': '2', 'WORD_SERVICE_BASE': 'http://localhost'})
    @mock.patch('entrystep.entrystep.WordService')
    @mock.patch('entrystep.entrystep.RandomPrefixService')
    def test_handler(self, random_prefix_service, word_service) -> None:
        words = ['a', 'ab', 'abc']
        random_prefix_service.return_value.random_prefix.return_value = 'a'
        word_service.return_value.starts_with.return_value = ['a', 'ab', 'abc']

        event = EntryStep().handler(
            {},
            None
        )
        self.assertEqual(event['startswith'], {'prefix': 'a', 'words': ['a', 'ab', 'abc']})
