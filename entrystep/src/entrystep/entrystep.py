import string
from pyawsstarter import LambdaBaseEnv
from .random_prefix_service import RandomPrefixService
from examplecommon import WordService


class EntryStep(LambdaBaseEnv):
    _letters = string.ascii_lowercase
    _number_letters = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__(
            {
                'MIN_CHARS': int,
                'MAX_CHARS': int,
                'WORD_SERVICE_BASE': str
            }
        )

        self._random_prefix_service = RandomPrefixService(
            self.get_parameter('MIN_CHARS'),
            self.get_parameter('MAX_CHARS')
        )

        self._word_service = WordService(self.get_parameter('WORD_SERVICE_BASE'))

    def handle(self, event, context) -> dict:
        prefix = self._random_prefix_service.random_prefix()
        self._logger.info('Searching for word prefix', prefix=prefix)
        event.update(
            {
                'startswith': {
                    'prefix': prefix,
                    'words': self._word_service.starts_with(prefix)
                }
            }
        )
        return event
