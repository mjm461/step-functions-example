from unittest import TestCase

from wordservice import create_app


class TestRoutes(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        app = create_app('flask_test.cfg')
        cls._test_client = app.test_client()

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
