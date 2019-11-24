import os
from .trie import Trie


class WordService(object):

    _resources_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), 'resources'))

    def __init__(self):
        self._trie = Trie()
        with open(os.path.join(self._resources_dir, 'words_alpha.txt')) as fin:
            for word in fin.read().split('\n'):
                if word:
                    self._trie.insert(word)

    def search(self, word):
        return self._trie.search(word)

    def starts_with(self, prefix, max_found=100):
        return self._trie.starts_with(prefix, max_found=max_found)
