# -*- coding: utf-8 -*-

__author__ = "Mark McClain"
__copyright__ = "Mark McClain"
__license__ = "mit"

import os
from moto import mock_s3

from unittest import TestCase, mock
from pyawsstarter import Clients
from storestep import StoreStep


class StoreStepTest(TestCase):

    @mock_s3
    @mock.patch.dict(os.environ, {'BUCKET_NAME': 'test-bucket'})
    def test_storestep(self) -> None:
        s3 = Clients.client('s3')
        s3.create_bucket(Bucket='test-bucket')
        StoreStep().handler({
            'startswith': {
                'prefix': 'a',
                'words': ['a', 'aa']
            }
        }, None)
