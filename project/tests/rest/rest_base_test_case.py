import base64
import logging
import unittest

import requests

from project.utilities.custom_logger import custom_logger


class RestBaseTestCase(unittest.TestCase):
    """
    When using this class:
    - Always add env dependencies in the main docstring.
    - Always verify the response.status_code
    - When expecting error, always verify the Exception (like ProjectSecurityUnauthorizedHMACException,
    InvalidMemberAuthException etc.)  and the ErrorCode
    """
    log = custom_logger(logging.DEBUG)

    def send_get_request_anonymous(self, device_id, get_request_path, hmac_token, expected_status_code):
        results = hmac_token.result
        print("results: {}".format(results))
        headers = {'timestamp': results['timestamp'], 'appkey': results['appkey'], 'hmac-sha1': results['hmac-sha1'],
                   'deviceID': device_id}
        response = requests.get(get_request_path, headers=headers)
        self.log_details_also_assert_status_code(expected_status_code, response)
        # The response's json method guesses which UTF encoding was used if no encoding was specified.
        # It converts a given string into a dictionary.
        return response.json()

    def send_get_request_anonymous_kipsu(self, device_id, get_request_path, hmac_token, expected_status_code):
        results = hmac_token.result
        print("results: {}".format(results))
        headers = {'timestamp': results['timestamp'], 'appkey': results['appkey'], 'hmac-sha1': results['hmac-sha1'],
                   'deviceID': device_id, 'proxyAuthKey': results['proxyAuthKey']}
        response = requests.get(get_request_path, headers=headers)
        self.log_details_also_assert_status_code(expected_status_code, response)
        # The response's json method guesses which UTF encoding was used if no encoding was specified.
        # It converts a given string into a dictionary.
        return response.json()

    def send_get_request_honors_member(self, device_id, get_request_path, hmac_token, expected_status_code,
                                       member_id, member_password):
        member_auth = base64.b64encode(bytes(member_id + ":" + member_password, 'utf-8'))
        results = hmac_token.result
        print("results: {}".format(results))
        headers = {'timestamp': results['timestamp'], 'appkey': results['appkey'], 'hmac-sha1': results['hmac-sha1'],
                   'deviceID': device_id, 'memberAuth': member_auth}
        response = requests.get(get_request_path, headers=headers)
        self.log_details_also_assert_status_code(expected_status_code, response)
        self.assertEqual(expected_status_code, response.status_code)
        return response.json()

    def send_post_request_honors_member(self, device_id, post_request_path, hmac_token,
                                        expected_status_code,
                                        member_id, member_password, data):
        member_auth = member_id + ":" + member_password
        encoded = base64.b64encode(bytes(member_auth, 'utf-8'))
        results = hmac_token.result
        print("results: {}".format(results))
        headers = {'timestamp': results['timestamp'], 'appkey': results['appkey'], 'hmac-sha1': results['hmac-sha1'],
                   'deviceID': device_id, 'memberAuth': encoded, 'content-type': 'application/json'}
        response = requests.post(post_request_path, headers=headers, data=data)
        self.log_details_also_assert_status_code(expected_status_code, response)
        if response.text:
            return response.json()

    def send_delete_request_honors_member(self, device_id, get_request_path, hmac_token, expected_status_code,
                                          member_id, member_password, data):
        member_auth = member_id + ":" + member_password
        encoded = base64.b64encode(bytes(member_auth, 'utf-8'))
        results = hmac_token.result
        print("results: {}".format(results))
        headers = {'timestamp': results['timestamp'], 'appKey': results['appkey'], 'hmac-sha1': results['hmac-sha1'],
                   'deviceID': device_id, 'memberAuth': encoded, 'content-type': 'application/json'}
        response = requests.delete(get_request_path, headers=headers, data=data)
        self.log_details_also_assert_status_code(expected_status_code, response)

    def assert_response_json_error_validation(self, response_json, error_type, error_code):
        self.log.debug(str(response_json))
        self.assertEqual(response_json['ErrorType'], error_type)
        self.assertEqual(str(response_json['ErrorCode']), error_code)

    def log_details_also_assert_status_code(self, expected_status_code, response):
        print(response.status_code)
        self.log.debug("Request URL: " + response.request.url)
        print(response.request.url)
        self.log.debug("Request headers: " + str(response.request.headers))
        print(str(response.request.headers))
        self.log.debug("Response status code: " + str(response.status_code))
        print(response.status_code)
        self.log.debug("Response JSON: " + str(response.text))
        print(str(response.text))
        self.assertEqual(expected_status_code, response.status_code)
