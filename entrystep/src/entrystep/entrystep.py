from awslambda import LambdaBaseEnv


class EntryStep(LambdaBaseEnv):

    def __init__(self):
        super().__init__(
            {
                'PARAM1': str,
                'PARAM2': int
            }
        )

    def handle(self, event, context) -> dict:
        event.update({
            'param1': self.get_parameter('PARAM1', 'param1'),
            'param2': self.get_parameter('PARAM2', 10),
        })

        return event
