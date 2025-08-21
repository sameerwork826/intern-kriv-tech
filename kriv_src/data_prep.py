
import pandas as pd
import os
from datetime import datetime
from kriv_src.utils import ensure_dir, save_df

def run_prep(input_path, output_dir):
    ensure_dir(output_dir)
    df = pd.read_csv(input_path, parse_dates=['order_date'])
    # basic cleaning
    df = df.drop_duplicates(subset=['order_id'])
    # derive weekday, month, year
    df['weekday'] = df['order_date'].dt.day_name()
    df['month'] = df['order_date'].dt.month
    df['year'] = df['order_date'].dt.year
    # convert is_cancelled to int
    df['is_cancelled'] = df['is_cancelled'].astype(int)
    save_df(df, os.path.join(output_dir, 'transactions_cleaned.csv'), index=False)
    return df

if __name__ == '__main__':
    run_prep('../data/pos_transactions.csv', '../outputs')
