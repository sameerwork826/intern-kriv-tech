
import pandas as pd
import os
from statsmodels.tsa.statespace.sarimax import SARIMAX
from kriv_src.utils import ensure_dir, save_df
import matplotlib.pyplot as plt

def run_forecast(clean_path, output_dir):
    ensure_dir(output_dir)
    df = pd.read_csv(clean_path, parse_dates=['order_date'])
    daily = df.groupby('order_date')['order_value'].sum().reset_index()
    daily = daily.set_index('order_date').asfreq('D').fillna(0)
    # simple SARIMAX fit (seasonal weekly)
    model = SARIMAX(daily['order_value'], order=(1,1,1), seasonal_order=(1,1,1,7), enforce_stationarity=False, enforce_invertibility=False)
    res = model.fit(disp=False)
    future = res.get_forecast(steps=28)
    pred = future.predicted_mean
    save_df(pred.reset_index().rename(columns={'index':'date',0:'predicted_revenue'}), os.path.join(output_dir,'weekly_revenue_forecast.csv'), index=False)
    # plot
    plt.figure(figsize=(10,5))
    plt.plot(daily.index[-60:], daily['order_value'][-60:], label='historical')
    plt.plot(pred.index, pred.values, label='forecast')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir,'revenue_forecast.png'))
    plt.close()
    return True

if __name__ == '__main__':
    run_forecast('../outputs/transactions_cleaned.csv','../outputs')
