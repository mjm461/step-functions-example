import collections


class TrieNode:
    def __init__(self):
        self._children = collections.defaultdict(TrieNode)
        self._is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current._children[letter]
        current._is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current._children.get(letter)
            if current is None:
                return False
        return current._is_word

    def _starts_with(self, prefix):
        current = self.root
        for letter in prefix:
            current = current._children.get(letter)
            if current is None:
                return None
        return current

    def starts_with(self, prefix, root=None, words=None, max_found=100):
        if not root:
            root = self._starts_with(prefix)

        words = words if words is not None else []

        if root and len(words) < max_found:
            if root._is_word:
                words.append(prefix)

            for letter, trie_node in root._children.items():
                self.starts_with(prefix + letter, root=trie_node, words=words, max_found=max_found)

        return words
