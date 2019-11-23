# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

from unittest import TestCase
from wordservice.trie import Trie

class TrieTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls._words = set([
            'a',
            'ab',
            'bad',
            'back',
            'test',
            'tester',
            'testing'
        ])

        cls._trie = Trie()
        for word in cls._words:
            cls._trie.insert(word)

    def test_not_found(self):
        found = self._trie.search('word')
        self.assertEqual(False, found)

    def test_found(self):
        found = self._trie.search('bad')
        self.assertEqual(True, found)

    def test_all_words(self):
        found = self._trie.starts_with('')
        self.assertEqual(0, len(set(found) ^ self._words))

    def test_prefix_words(self):
        found = self._trie.starts_with('test')
        self.assertEqual(0, len(set(found) ^ set(['test', 'tester', 'testing'])))

    def test_prefix_max_found(self):
        found = self._trie.starts_with('test', max_found=2)
        self.assertEqual(2, len(found))
