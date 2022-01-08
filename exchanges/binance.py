import requests
from utils.customLogger import logger
from utils.customDatetime import ms_datetime

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

    def get_data(self, symbol, interval, start_time=None, end_time=None, limit=1000):
        endpoint = "/api/v3/klines"
        query_params = {"symbol": symbol, "interval": interval, "limit": limit}

        if start_time is not None:
            query_params["startTime"] = start_time
        if end_time is not None:
            query_params["endTime"] = end_time

        response = self._make_request(endpoint, query_params=query_params)
        if response is not None:
            logger.info(f"Data Retrieved for {symbol} from {ms_datetime(response[0][0])} to {ms_datetime(response[-1][0])}")

        return response

