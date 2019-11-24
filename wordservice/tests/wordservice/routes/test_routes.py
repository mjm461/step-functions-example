import os
from unittest import TestCase, mock

from wordservice import create_app, WordService


class TestRoutes(TestCase):

    _resources_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'resources'))

    @classmethod
    def setUpClass(cls) -> None:

        with mock.patch.object(WordService, '_resources_dir', cls._resources_dir):
            app = create_app('flask_test.cfg')
            cls._test_client = app.test_client()

            # WordService is a singleton that gets inject on the first call, so
            # this line primes the singleton
            cls._test_client.get(
                '/search?word=prime'
            )

    def test_search(self):

        response = self._test_client.get(
            '/search?word=word'
        )
        self.assertTrue(response.json['found'])

    def test_startswith(self):

        response = self._test_client.get(
            '/startswith?prefix=word'
        )
        self.assertTrue(len(response.json['words']) > 0)
