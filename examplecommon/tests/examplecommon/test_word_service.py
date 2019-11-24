# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import json
from unittest import TestCase
import responses

from examplecommon import WordService, WordServiceException


class TestWordService(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._word_service = WordService('http://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @responses.activate
    def test_word_service_success(self) -> None:
        def request_callback(request):
            assert request
            return (200, {}, json.dumps({'words': ['a', 'ab', 'abc']}))

        responses.add_callback(
            responses.GET, 'http://localhost/startswith?prefix=a',
            callback=request_callback,
            content_type='application/json',
            match_querystring=True
        )

        words = self._word_service.starts_with('a')

        self.assertEqual(3, len(words))

    @responses.activate
    def test_word_service_failed_connetion(self) -> None:

        with self.assertRaises(WordServiceException):
            self._word_service.starts_with('a')

    @responses.activate
    def test_word_service_404(self) -> None:

        responses.add(
            responses.GET, 'http://localhost/startswith?prefix=a',
            json={'error': 'not found'},
            status=404
        )

        with self.assertRaises(WordServiceException):
            self._word_service.starts_with('a')
