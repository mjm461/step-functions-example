# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os
from unittest import TestCase, mock
from wordservice import WordService


class TrieTest(TestCase):

    _resources_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), 'resources'))

    @classmethod
    def setUpClass(cls) -> None:
        with mock.patch.object(WordService, '_resources_dir', cls._resources_dir):
            cls._word_service = WordService()

    def test_not_found(self):
        found = self._word_service.search('wordthatdoesnotexist')
        self.assertEqual(False, found)

    def test_found(self):
        found = self._word_service.search('word')
        self.assertEqual(True, found)

    def test_starts_with_not_found(self):
        found = self._word_service.starts_with('wordthatdoesnotexist')
        self.assertEqual(0, len(found))

    def test_starts_with_found(self):
        found = self._word_service.starts_with('word')
        assert len(found)

    def test_starts_with_maxfound(self):
        found = self._word_service.starts_with('w', max_found=10)
        self.assertEqual(10, len(found))
