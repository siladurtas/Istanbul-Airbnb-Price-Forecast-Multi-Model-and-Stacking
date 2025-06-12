import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path, compression='gzip', low_memory=False)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()