
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from kriv_src.utils import ensure_dir, save_df

def run_eda(clean_path, output_dir):
    ensure_dir(output_dir)
    df = pd.read_csv(clean_path, parse_dates=['order_date'])
    # overall KPIs
    total_orders = len(df)
    total_cancelled = df['is_cancelled'].sum()
    avg_order_value = df['order_value'].mean()
    kpis = {'total_orders': total_orders, 'total_cancelled': int(total_cancelled), 'avg_order_value': round(float(avg_order_value),2)}
    save_df(pd.DataFrame([kpis]), os.path.join(output_dir,'kpis_summary.csv'), index=False)
    # top menus by revenue
    top_menu = df.groupby('menu_item')['order_value'].sum().sort_values(ascending=False).reset_index()
    save_df(top_menu, os.path.join(output_dir,'top_menu_revenue.csv'), index=False)
    # cancellations by delivery time bins
    bins = [0,15,20,25,30,40,100]
    df['del_bin'] = pd.cut(df['delivery_time_min'], bins=bins)
    cancel_by_bin = df.groupby('del_bin')['is_cancelled'].mean().reset_index()
    save_df(cancel_by_bin, os.path.join(output_dir,'cancel_by_delivery_bin.csv'), index=False)
    # plots
    plt.figure(figsize=(8,5))
    sns.barplot(data=top_menu.head(10), x='menu_item', y='order_value')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir,'top_menu_revenue.png'))
    plt.close()

    plt.figure(figsize=(8,5))
    daily = df.groupby('order_date')['order_value'].sum().reset_index()
    sns.lineplot(data=daily, x='order_date', y='order_value')
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir,'daily_revenue.png'))
    plt.close()
    return kpis

if __name__ == '__main__':
    run_eda('../outputs/transactions_cleaned.csv','../outputs')
