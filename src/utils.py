import requests
from requests_negotiate_sspi import HttpNegotiateAuth

requests.urllib3.disable_warnings()


ENV = {"local": "http:/localhost:8000", "prod": ""}

HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer {token}"}

ENDPOINTS = {"get_data": "/api/connection/get_data?connection_id={id}"}


class Api:
    _server: str = None
    _endpoint: str = None

    def __init__(self, server: str = None, endpoint: str = None) -> None:
        self.server = server
        self.endpoint = endpoint

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server: str):
        self._server = ENV[server]

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        self._endpoint = ENDPOINTS[endpoint]

    def get_data(self) -> requests.Response:
        response = requests.get(
            f"{self.server}{self.endpoint}", headers=HEADERS, auth=HttpNegotiateAuth()
        )
        return response
