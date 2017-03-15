import warnings

from requests.packages.urllib3.exceptions import InsecureRequestWarning

from common.base import BaseTest
import requests


class BasePostTest(BaseTest):
    def __init__(self, url, test_data, expected_code):
        super(BasePostTest, self).__init__(url, test_data, expected_code)

    def launch(self):
        BaseTest.run(self, post(self._url, self._test_request_data, self._test_request_header))


def post(url, test_request_data, test_request_header):
    warnings.filterwarnings('ignore', category=InsecureRequestWarning)

    return requests.post(url, json=test_request_data,
                         headers=test_request_header,
                         verify=False)
