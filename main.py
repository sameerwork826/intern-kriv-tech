
from kriv_src.data_prep import run_prep
from kriv_src.eda import run_eda
from kriv_src.clustering import run_clustering
from kriv_src.cancel_model import run_cancel_model
from kriv_src.forecasting import run_forecast
import os

def main():
    base = os.path.dirname(__file__)
    data_path = os.path.join(base,'data','pos_transactions.csv')
    outputs = os.path.join(base,'outputs')
    df = run_prep(data_path, outputs)
    run_eda(os.path.join(outputs,'transactions_cleaned.csv'), outputs)
    run_clustering(os.path.join(outputs,'transactions_cleaned.csv'), outputs)
    auc = run_cancel_model(os.path.join(outputs,'transactions_cleaned.csv'), outputs)
    run_forecast(os.path.join(outputs,'transactions_cleaned.csv'), outputs)
    print('Pipeline complete. AUC for cancellation model:', auc)

if __name__ == '__main__':
    main()
