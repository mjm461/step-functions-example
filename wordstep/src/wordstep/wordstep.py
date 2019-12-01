import string
from pyawsstarter import LambdaBaseEnv
from .random_prefix_service import RandomPrefixService
from examplecommon import WordService


class WordsNotFoundException(Exception):
    pass


class WordStep(LambdaBaseEnv):
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
        # uses prefix if give, else create a random one
        prefix = event.get('prefix') or self._random_prefix_service.random_prefix()

        self._logger.info('Searching for word prefix', prefix=prefix)
        words = self._word_service.starts_with(prefix)

        if not words:
            raise WordsNotFoundException('No words found for prefix: '.format(prefix))

        event.update(
            {
                'startswith': {
                    'prefix': prefix,
                    'words': words
                }
            }
        )
        return event
