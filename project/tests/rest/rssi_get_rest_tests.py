from os import environ
import pprint
from project.tests.rest.rest_base_test_case import RestBaseTestCase
from project.utilities.rest import HMSTokenClient


class RssiGetRestTests(RestBaseTestCase):
    """
    Test cases about the RSSI Get method - see https://
    Please also visit: https://jira.

    """

    @classmethod
    def setUpClass(cls):
        cls.base_path = environ.get("base_path")
        cls.client = HMSTokenClient(environ.get("console_username"), environ.get("console_password"),
                                    cls.base_path)

        cls.device_id_android = 'Droid_PRODUCTION'
        cls.device_id_ios = '4b21428e503a7c8b8ed298c4da2cad2b71b19c43'
        cls.device_id_no_os = 'd9231c93cda36963abcf1217c8a40411'
        cls.expected_android_default_value = '67.891'
        cls.expected_android_default_value_test_attribute = '-0.77'
        cls.expected_ios_default_value = '123.45'
        cls.expected_no_os_default_value = '123.45'

        cls.rssi_path = "http://{}".format(cls.base_path) + '/hms/v1/core/rssi?ctyhocn='

    def test_rssi_get_happy_path_invalid_ctyhocn_list_android_device(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        invalid_ctyhocn_list = 'commaDelimitedCtyhocns'
        invalid_rssi_path = self.rssi_path + invalid_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_android, invalid_rssi_path, hmac_token, 200)
        pprint.pprint(response_json)

        self.assertEqual(response_json[0]['attributes']['test_attribute'], self.expected_android_default_value)

    def test_rssi_get_happy_path_invalid_ctyhocn_list_ios_device(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        invalid_ctyhocn_list = 'commaDelimitedCtyhocns'
        invalid_rssi_path = self.rssi_path + invalid_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_ios, invalid_rssi_path, hmac_token, 200)
        pprint.pprint(response_json)

        self.assertEqual(response_json[0]['attributes']['test_attribute'], self.expected_ios_default_value)

    def test_rssi_get_happy_path_invalid_ctyhocn_list_no_os_device(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        invalid_ctyhocn_list = 'commaDelimitedCtyhocns'
        invalid_rssi_path = self.rssi_path + invalid_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_no_os, invalid_rssi_path, hmac_token, 400)
        pprint.pprint(response_json)

        # We expect OsTypeInvalid exception, no ErrorCode
        self.assert_response_json_error_validation(response_json, 'OsTypeInvalidException', "None")

    def test_rssi_get_happy_path_dalmagi_android_device(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        single_ctyhocn_list = 'DALMAGI'
        single_ctyhocn_list_path = self.rssi_path + single_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_android, single_ctyhocn_list_path, hmac_token,
                                                        200)
        pprint.pprint(response_json)

        self.assertEqual(response_json[0]['attributes']['test_attribute'],
                         self.expected_android_default_value_test_attribute)

    def test_rssi_get_empty_ctyhocn_android_device_precondition_failed(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        empty_ctyhocn_list = ''
        empty_ctyhocn_list_path = self.rssi_path + empty_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_android, empty_ctyhocn_list_path, hmac_token,
                                                        412)
        pprint.pprint(response_json)

        # We expect CtyhocnMissingException exception, no ErrorCode
        self.assert_response_json_error_validation(response_json, 'CtyhocnMissingException', "None")

    def test_rssi_get_no_ctyhocn_android_device_bad_request(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        empty_ctyhocn_list_path = "http://{}".format(self.base_path) + '/hms/v1/core/rssi'

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(self.device_id_android, empty_ctyhocn_list_path, hmac_token,
                                                        400)
        pprint.pprint(response_json)

        # We expect HMSException exception
        self.assert_response_json_error_validation(response_json, 'HMSException', '-1')

    def test_rssi_get_no_device_bad_request(self):
        self.client.authenticate()
        hmac_token = self.client.get_hmac("REST_METHOD_RSSI")
        single_ctyhocn_list = 'DALMAGI'
        single_ctyhocn_list_path = self.rssi_path + single_ctyhocn_list

        # Sending the path for the GET request along with the headers and the expected response code.
        response_json = self.send_get_request_anonymous(None, single_ctyhocn_list_path, hmac_token,
                                                        400)
        pprint.pprint(response_json)

        # We expect HMSException exception
        self.assert_response_json_error_validation(response_json, 'HMSException', '-1')
