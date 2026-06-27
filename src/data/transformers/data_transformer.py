import pandas as pd
import numpy as np


class DataTransformer:
    def add_returns(self, df):
        df = df.copy()
        df["Returns"] = df["Close"].pct_change()
        return df

    def add_log_returns(self, df):
        df = df.copy()
        df["Log_Returns"] = np.log(
            df["Close"] / df["Close"].shift(1)
        )
        return df

    def add_moving_average(self, df, window=20):
        df = df.copy()
        df[f"MA_{window}"] = (
            df["Close"]
            .rolling(window=window)
            .mean()
        )
        return df

    def add_volatility(self, df, window=20):
        df = df.copy()

        if "Returns" not in df.columns:
            df["Returns"] = df["Close"].pct_change()

        df[f"Volatility_{window}"] = (
            df["Returns"]
            .rolling(window=window)
            .std()
        )

        return df