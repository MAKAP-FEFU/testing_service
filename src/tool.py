from .utils import ENDPOINTS, Api


def get_data(server: str = "local"):
    api = Api(server=server)
    api.endpoint = ENDPOINTS["get_data"]

    response = api.get_data()

    result = response.json()
    return result
