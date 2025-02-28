import pandas as pd

# Load the cleaned data
def load_data(file_path):
    return pd.read_csv(file_path)

# Calculate defect rate
def calculate_defect_rate(defect_data):
    defect_data['defect_rate'] = defect_data['inspection_result'].apply(lambda x: 1 if x == 'Fail' else 0)
    defect_rate = defect_data.groupby('production_id')['defect_rate'].mean()
    return defect_rate

# Example usage
if __name__ == "__main__":
    defect_data = load_data('data/processed_data/cleaned_defect_data.csv')
    defect_rate = calculate_defect_rate(defect_data)
    print(defect_rate)
