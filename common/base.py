import ssl
import warnings


class BaseTest(object):
    def __init__(self, url, test_data, expected_code):
        self._url = url
        self._test_request_header = test_data['header']
        self._test_request_data = test_data['body']
        self._expected_code = expected_code

    def run(self, response):
        print('Request header: ' + str(self._test_request_header))
        print('Request body: ' + str(self._test_request_data))
        print('-' * 20 + 'SENDING REQUEST...' + '-' * 20)
        try:
            assert (
                self._expected_code == response.status_code), "Service responded the {} code, but expected one was {}" \
                .format(str(response.status_code), str(self._expected_code))
        except AssertionError as e:
            warnings.warn(e.args[0])
        print('Service responded the ' + str(response.status_code) + ' code')
        print('Response header: ' + str(response.headers))
        print('Response body: ' + str(response.content))
