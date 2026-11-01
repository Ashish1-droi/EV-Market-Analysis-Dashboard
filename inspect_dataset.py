
import pandas as pd


# Load the EV dataset
file_path = "data/electric_vehicles_spec_2025.csv"
df = pd.read_csv('electric_vehicles_spec_2025.csv')

# Display basic information
print("\nDATASET LOADED SUCCESSFULLY")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())
