from .utils import ENDPOINTS, Api


def get_data(server: str = "local", token: str = "") -> dict[str, list]:
    api = Api(server=server, token=token)
    api.endpoint = ENDPOINTS["get_data"]

    response = api.get_data()

    result = response.json()
    return result
