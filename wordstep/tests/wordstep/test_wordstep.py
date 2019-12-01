# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os

from unittest import TestCase, mock
from wordstep import WordStep, WordsNotFoundException


class HandlerTest(TestCase):

    @mock.patch.dict(os.environ, {'MIN_CHARS': '2', 'MAX_CHARS': '2', 'WORD_SERVICE_BASE': 'http://localhost'})
    @mock.patch('wordstep.wordstep.WordService')
    @mock.patch('wordstep.wordstep.RandomPrefixService')
    def test_wordstep_success(self, random_prefix_service, word_service) -> None:
        random_prefix_service.return_value.random_prefix.return_value = 'a'
        word_service.return_value.starts_with.return_value = ['a', 'ab', 'abc']

        event = WordStep().handler(
            {},
            None
        )
        self.assertEqual(event['startswith'], {'prefix': 'a', 'words': ['a', 'ab', 'abc']})

    @mock.patch.dict(os.environ, {'MIN_CHARS': '2', 'MAX_CHARS': '2', 'WORD_SERVICE_BASE': 'http://localhost'})
    @mock.patch('wordstep.wordstep.WordService')
    @mock.patch('wordstep.wordstep.RandomPrefixService')
    def test_wordstep_notfound(self, random_prefix_service, word_service) -> None:
        random_prefix_service.return_value.random_prefix.return_value = 'a'
        word_service.return_value.starts_with.return_value = []

        with self.assertRaises(WordsNotFoundException):
            WordStep().handler({}, None)
