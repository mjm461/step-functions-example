from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException, HTTPError

from pyawsstarter import Logger


class WordServiceException(Exception):
    pass


class WordService(object):

    _starts_with_path = '/startswith?prefix={}'

    def __init__(self, base_url, logger=None):
        self._base_url = base_url
        if not logger:
            self._logger = Logger.get_logger('wordservice')

    def starts_with(self, prefix) -> None:
        """Wrapper to call the starts with API
        Args:
            prefix (str) Prefix of the word to ask for.

        Returns:
            list[str]: The list of words with that prefix.

        Raises:
            WordServiceException: Log anything that is "wrong" and raise.
        """
        try:
            response = requests.get(urljoin(self._base_url, self._starts_with_path.format(prefix)))
            if response.status_code == 200:
                return response.json()['words']
        except (HTTPError, RequestException) as e:
            self._logger.warn('Error requesting wordservice.starts_with', prefix=prefix, exception=str(e))

        raise WordServiceException("No words found for prefix: {}".format(prefix))
