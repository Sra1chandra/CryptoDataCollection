from utils.customLogger import logger

from exchanges.binance import BinanceAPI

if __name__ == "__main__":
    client = BinanceAPI()
    data = client.get_data('BTCUSDT', '1m')
    print(len(data))
