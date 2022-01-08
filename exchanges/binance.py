import requests
from utils.customLogger import logger

class BinanceAPI:
    def __init__(self):
        self._baseurl = "https://api.binance.com"
        pass

    def _make_request(self, endpoint, query_params=None):
        response = requests.get(self._baseurl+endpoint, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Request error when connecting to {self._baseurl+endpoint}")
            return None

    def get_symbols(self):
        endpoint = "/api/v3/exchangeInfo"
        response = self._make_request(endpoint)
        symbols_list = [record["symbol"] for record in response["symbols"]]
        return symbols_list

