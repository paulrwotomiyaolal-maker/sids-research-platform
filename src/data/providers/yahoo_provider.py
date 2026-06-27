import yfinance as yf
import pandas as pd


class YahooFinanceProvider:
    """
    Downloads market data from Yahoo Finance.
    """

    def fetch(
        self,
        ticker: str,
        start: str,
        end: str,
        interval: str = "1d",
    ) -> pd.DataFrame:
        df = yf.download(
            ticker,
            start=start,
            end=end,
            interval=interval,
            auto_adjust=True,
            progress=False,
        )

        return df