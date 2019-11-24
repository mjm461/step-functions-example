import string
from pyawsstarter import LambdaBaseEnv
from .random_prefix_service import RandomPrefixService


class EntryStep(LambdaBaseEnv):
    _letters = string.ascii_lowercase
    _number_letters = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__(
            {
                'MIN_CHARS': int,
                'MAX_CHARS': int
            }
        )

        self._random_prefix_service = RandomPrefixService(
            self.get_parameter('MIN_CHARS'),
            self.get_parameter('MAX_CHARS')
        )

    def handle(self, event, context) -> dict:

        event.update(
            {
                'prefix': self._random_prefix_service.random_prefix()
            }
        )

        return event
