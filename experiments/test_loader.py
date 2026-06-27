from src.data.loaders.csv_loader import CSVLoader

loader = CSVLoader()

df = loader.load("AAPL.csv")

print(df.head())
print()
print(df.tail())
print()
print(df.shape)