from pathlib import Path


class CSVStorage:
    def __init__(self, base_dir="data/raw"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save(self, df, filename):
        path = self.base_dir / filename
        df.to_csv(path)
        return path