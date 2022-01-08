from utils.customLogger import logger
from exchanges.binance import BinanceAPI

if __name__ == "__main__":
    client = BinanceAPI()
    symbols_list = client.get_symbols()
    print(len(symbols_list))
