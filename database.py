import h5py
import numpy as np
import pandas as pd

class HDF5Client:
    def __init__(self, exchange):
        self.hf = h5py.File(f"data/{exchange}.h5", "a")
        self.hf.flush()

    def create_dataset(self, symbol):
        if symbol not in self.hf.keys():
            self.hf.create_dataset(symbol, (0, 6), maxshape=(None, 6), dtype="float64")
            self.hf.flush()

    def write_data(self, symbol, data):
        np_data = np.array(data)
        if symbol not in self.hf.keys():
            self.create_dataset(symbol)

        if len(np_data) != 0:
            self.hf[symbol].resize(self.hf[symbol].shape[0]+np_data.shape[0], axis=0)
            self.hf[symbol][-np_data.shape[0]:] = np_data
            self.hf.flush()

    def read_data(self, symbol):
        hdf5_data = self.hf[symbol]
        np_data = np.array(hdf5_data)

        df = pd.DataFrame(np_data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"].values.astype(np.int64), unit="ms")
        return df

    def min_max_timestamp(self, symbol):
        existing_data = self.hf[symbol]

        if len(existing_data) == 0:
            return None, None

        min_timestamp = min(existing_data, key=lambda x: x[0])[0]
        max_timestamp = max(existing_data, key=lambda x: x[0])[0]

        return min_timestamp, max_timestamp





