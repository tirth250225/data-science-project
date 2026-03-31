import pandas as pd
from config import FILE_PATH

def load_data():
    df = pd.read_csv(FILE_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df