from src.data.loaders.csv_loader import CSVLoader
from src.data.transformers.data_transformer import DataTransformer

loader = CSVLoader()
transformer = DataTransformer()

df = loader.load("AAPL.csv")

df = transformer.add_returns(df)
df = transformer.add_log_returns(df)
df = transformer.add_moving_average(df, window=20)
df = transformer.add_volatility(df, window=20)

print(df.head(25))
print()
print(df.columns)
print()
print(df.shape)