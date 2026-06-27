from pathlib import Path
import pandas as pd


class CSVLoader:
    def __init__(self, base_dir="data/raw"):
        self.base_dir = Path(base_dir)

    def load(self, filename):
        path = self.base_dir / filename

        df = pd.read_csv(
            path,
            skiprows=[1, 2]
        )

        df["Price"] = pd.to_datetime(df["Price"])
        df = df.rename(columns={"Price": "Date"})
        df = df.set_index("Date")

        return df