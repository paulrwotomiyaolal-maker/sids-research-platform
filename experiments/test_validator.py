from src.data.loaders.csv_loader import CSVLoader
from src.data.validators.data_validator import DataValidator


loader = CSVLoader()
validator = DataValidator()

df = loader.load("AAPL.csv")

validator.validate(df)

print("Validation passed.")
print(df.shape)