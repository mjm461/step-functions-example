# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

from unittest import TestCase, mock
from entrystep.random_prefix_service import RandomPrefixService


class RandomPrefixServiceTest(TestCase):

    @mock.patch('random.randint')
    def test_random_prefix(self, random_int):
        random_int.side_effect = [
            2,  # first call is num chars
            0,  # second is index of a
            1  # third is index of b
        ]

        service = RandomPrefixService(2, 4)
        prefix = service.random_prefix()

        self.assertTrue('ab', prefix)
