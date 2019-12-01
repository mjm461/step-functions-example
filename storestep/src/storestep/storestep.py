from pyawsstarter import LambdaBaseEnv, Clients


class StoreStep(LambdaBaseEnv):

    def __init__(self):
        super().__init__(
            {
                'BUCKET_NAME': str
            }
        )

        self._bucket_name = self.get_parameter('BUCKET_NAME')
        self._s3 = Clients.client('s3')

    def handle(self, event, _context) -> dict:

        prefix = event['startswith']['prefix']
        words = event['startswith']['words']

        self._s3.put_object(
            Body='\n'.join(words).encode('utf-8'),
            Bucket=self._bucket_name,
            Key=prefix
        )
