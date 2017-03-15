from common.base import BaseTest
import requests
import warnings


class BaseDeleteTest(BaseTest):
    def __init__(self, url, test_data, expected_code):
        super(BaseDeleteTest, self).__init__(url, test_data, expected_code)

    def launch(self):
        warnings.filterwarnings('ignore', category=DeprecationWarning)

        BaseTest.run(self,
                     requests.delete(self._url, headers=self._test_request_header,
                                     data=self._test_request_data, verify=False))
