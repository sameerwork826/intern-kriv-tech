
import os
import pandas as pd

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)
    return path

def save_df(df, path: str, index=False):
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=index)
