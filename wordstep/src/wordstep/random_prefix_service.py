import random
import string


class RandomPrefixService(object):

    _letters = string.ascii_lowercase
    _number_letters = len(string.ascii_lowercase)

    def __init__(self, min_chars, max_chars):
        self._min_chars = min_chars
        self._max_chars = max_chars

    def random_prefix(self) -> str:
        return "".join(
            [
                self._letters[random.randint(0, self._number_letters-1)]
                for _ in range(random.randint(self._min_chars, self._max_chars))
            ]
        )
