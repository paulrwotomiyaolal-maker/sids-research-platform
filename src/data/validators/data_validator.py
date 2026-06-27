import pandas as pd


class DataValidator:
    REQUIRED_COLUMNS = [
        "Close",
        "High",
        "Low",
        "Open",
        "Volume",
    ]

    def validate(self, df: pd.DataFrame):
        self._validate_empty(df)
        self._validate_columns(df)
        self._validate_missing(df)
        self._validate_duplicates(df)
        self._validate_date_order(df)

    def _validate_empty(self, df):
        if df.empty:
            raise ValueError("Dataset is empty.")

    def _validate_columns(self, df):
        missing = [
            col
            for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

    def _validate_missing(self, df):
        if df.isnull().sum().sum() > 0:
            raise ValueError(
                "Dataset contains missing values."
            )

    def _validate_duplicates(self, df):
        if df.index.duplicated().any():
            raise ValueError(
                "Duplicate dates detected."
            )

    def _validate_date_order(self, df):
        if not df.index.is_monotonic_increasing:
            raise ValueError(
                "Dates are not sorted."
            )