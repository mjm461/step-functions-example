import string
from pyawsstarter import LambdaBaseEnv


class Template(LambdaBaseEnv):
    _letters = string.ascii_lowercase
    _number_letters = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__(
            {
                'PARAM_INT': int,
                'PARAM_INT': str
            }
        )

    def handle(self, event, _context) -> dict:
        return event
