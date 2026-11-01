
import pandas as pd

print("========== EV DATA CLEANING STARTED ==========")

# 1. Load original dataset
input_file = "data/electric_vehicles_spec_2025.csv"

df = pd.read_csv(input_file)

print("\nOriginal Dataset Shape:", df.shape)

# 2. Remove unnecessary spaces from text columns
text_columns = df.select_dtypes(include=["object", "str"]).columns

for column in text_columns:
    df[column] = df[column].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# 3. Handle missing model name
df["model"] = df["model"].fillna("Unknown model")

# 4. Convert numerical columns into correct data types
numeric_columns = [
    "top_speed_kmh",
    "battery_capacity_kWh",
    "number_of_cells",
    "torque_nm",
    "efficiency_wh_per_km",
    "range_km",
    "acceleration_0_100_s",
    "fast_charging_power_kw_dc",
    "towing_capacity_kg",
    "seats",
    "length_mm",
    "width_mm",
    "height_mm"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 5. Create a numerical cargo volume column
# Keep the original cargo_volume_l column unchanged.
df["cargo_volume_l_numeric"] = pd.to_numeric(
    df["cargo_volume_l"],
    errors="coerce"
)

# 6. Check duplicate records
duplicates = df.duplicated().sum()

print("\nDuplicate Records Found:", duplicates)

df = df.drop_duplicates()

# 7. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 8. Check invalid numerical values
positive_columns = [
    "top_speed_kmh",
    "battery_capacity_kWh",
    "efficiency_wh_per_km",
    "range_km",
    "acceleration_0_100_s",
    "seats",
    "length_mm",
    "width_mm",
    "height_mm"
]

for column in positive_columns:
    invalid_count = (df[column] <= 0).sum()
    print(f"{column}: {invalid_count} invalid values")

# 9. Save cleaned dataset
output_file = "data/electric_vehicles_cleaned.csv"

df.to_csv(output_file, index=False)

# 10. Final summary
print("\n========== CLEANING SUMMARY ==========")

print("Original Records: 477")
print("Final Records:", len(df))
print("Final Columns:", len(df.columns))

print("\nCleaned Dataset Saved Successfully!")
print("File Location:", output_file)

print("\n========== DATA CLEANING COMPLETED ==========")
