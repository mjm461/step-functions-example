# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

from wordservice import WordService
from unittest import TestCase


class TrieTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
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
        found = self._word_service.starts_with('a', max_found=100)
        self.assertEqual(100, len(found))

    def test_starts_with_maxfound(self):
        found = self._word_service.starts_with('a', max_found=100)
        self.assertEqual(100, len(found))
