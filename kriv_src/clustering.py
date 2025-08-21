
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from kriv_src.utils import ensure_dir, save_df
import os

def run_clustering(clean_path, output_dir):
    ensure_dir(output_dir)
    df = pd.read_csv(clean_path, parse_dates=['order_date'])
    # customer-level aggregation
    cust = df.groupby('customer_id').agg({'order_id':'count','order_value':'mean'}).rename(columns={'order_id':'order_count','order_value':'avg_order_value'}).reset_index()
    # take top customers for stability
    cust_sample = cust[cust['order_count']>1]
    X = cust_sample[['order_count','avg_order_value']].fillna(0)
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    cust_sample['cluster'] = kmeans.labels_
    save_df(cust_sample, os.path.join(output_dir,'customer_clusters.csv'), index=False)
    return cust_sample

if __name__ == '__main__':
    run_clustering('../outputs/transactions_cleaned.csv','../outputs')
