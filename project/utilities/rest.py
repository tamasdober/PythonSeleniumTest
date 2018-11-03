import time

import requests

TOKEN_DURATION_MINUTES = 15


class TokenClient:
    """
    This is a lightweight client used to retrieve various credentials needed to
    make rest calls against Project endpoints. All tokens are returned in Token wrapper objects.
    """

    @property
    def hmac_path(self):
        return "/console/debug/hmacresult?restMethod={}"

    @property
    def member_auth_path(self):
        return "/console/debug/memberauthresult?id={}&pass={}"

    @property
    def cust_auth_path(self):
        return "/console/debug/authcustresult?id={}&pass={}"

    @property
    def cust_anon_path(self):
        return "/console/debug/anoncustresult?guestId={}"

    @property
    def authorization_path(self):
        return "/console/j_spring_security_check"

    @property
    def success_path(self):
        return "/console/welcome"

    def __init__(self, username, password, base_path):
        self.payload = {
            "username": username,
            "password": password
        }
        self.path = "http://{}".format(base_path)
        self.session = requests.Session()
        self._auth_time = None

    def authenticate(self):
        """
        Method used to authenticate the user
        :return: the result of whether the login was successful or not
        """
        res = self.session.post(self.path + self.authorization_path, data=self.payload)
        if res.url == self.path + self.success_path:
            self._auth_time = time.time()
            return True
        else:
            return False

    def get_hmac(self, rest_method):
        """
        Will return a token for the rest method specified. The result is stored in the Token as
        a dictionary, therefore to retrieve a particular value you must specify a key, i.e. token.result['hmac-sha1']
        :param rest_method: A string of the rest method you need a token for
        :return:
        """
        path = self.path + self.hmac_path.format(rest_method)
        response = self.session.get(path)
        if response.request.url != path:
            raise UnauthorizedAccessException(
                "You are not authorized to reach page: {}".format(path)
            )
        if response.text == "":
            raise InvalidEndpointException("{} is not an available rest method".format(rest_method))
        return _Token(time.time(), _jsonify(response.text))

    def get_member_auth(self, honors_id, password):
        """
        Will return a member auth token. Result is stored in the token as a simple string.
        :param honors_id:
        :param password:
        :return:
        """
        path = self.path + self.member_auth_path.format(honors_id, password)
        response = self.session.get(path)
        if response.request.url != path:
            raise UnauthorizedAccessException(
                "You are not authorized to reach page: {}".format(path)
            )
        return _Token(time.time(), response.text)

    def get_customer_auth(self, honors_id, password):
        """
        Will return a customer auth token. Result is stored in the token as a simple string.
        :param honors_id:
        :param password:
        :return:
        """
        path = self.path + self.cust_auth_path.format(honors_id, password)
        response = self.session.get(path)
        if response.request.url != path:
            raise UnauthorizedAccessException(
                "You are not authorized to reach page: {}".format(path)
            )
        return _Token(time.time(), response.text)

    def get_customer_anon(self, guest_id):
        """
        Will return a customer anon token. Result is stored in the token as a simple string.
        :param guest_id:
        :return:
        """
        path = self.path + self.cust_anon_path.format(guest_id)
        response = self.session.get(path)
        if response.request.url != path:
            raise UnauthorizedAccessException(
                "You are not authorized to reach page: {}".format(path)
            )
        return _Token(time.time(), response.text)

    def is_expired(self):
        """
        Method that will return whether this client is expired.
        :return: true or false
        """
        response = self.session.get(self.path + self.success_path)
        return response.request.path_url != self.success_path


class UnauthorizedAccessException(Exception):
    """
    Raise for attempting to retrieve tokens without authorization
    """


class InvalidEndpointException(Exception):
    """
    Raise when attempting to hit an endpoint that isn't returning any valid data.
    """


class _Token:
    """
    A Token object acts as a wrapper for the data you retrieve from the various authorization
    generators in the hmac page.
    """

    def __init__(self, timestamp, result):
        self._timestamp = timestamp
        self.result = result

    def is_expired(self):
        now = time.time()
        return (now - self._timestamp) / 60 > TOKEN_DURATION_MINUTES


def _jsonify(line_separated_string):
    """
    Function that will transform a string of key/value pairs separated by line breaks into a dict
    :param line_separated_string: A response with each key/value pair seperated by line breaks
    :return: A jsonified version of the input
    """
    json_response = dict()
    pairs = line_separated_string.split("\n")
    for x in pairs:
        decon_key_value_pair = x.partition(":")
        # If there is a key or value missing, continue
        if '' in decon_key_value_pair:
            continue
        json_response[decon_key_value_pair[0]] = decon_key_value_pair[2]
    return json_response
