import pandas as pd
import numpy as np

# Load the raw data
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean the data: Remove duplicates and handle missing values
def clean_data(data):
    data.drop_duplicates(inplace=True)
    data.fillna(method='ffill', inplace=True)
    return data

# Save the cleaned data
def save_data(data, output_path):
    data.to_csv(output_path, index=False)

# Example usage
if __name__ == "__main__":
    production_data = load_data('data/raw_data/production_logs.csv')
    cleaned_production_data = clean_data(production_data)
    save_data(cleaned_production_data, 'data/processed_data/cleaned_production_data.csv')
