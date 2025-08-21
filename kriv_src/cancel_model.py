
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report
from kriv_src.utils import ensure_dir, save_df
import joblib

def run_cancel_model(clean_path, output_dir):
    ensure_dir(output_dir)
    df = pd.read_csv(clean_path, parse_dates=['order_date'])
    # features
    df['hour'] = pd.to_datetime(df['order_date']).dt.hour
    X = df[['order_value','delivery_time_min','quantity','promo_flag']].fillna(0)
    y = df['is_cancelled']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
    preds = model.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, preds)
    # save model and results
    save_df(pd.DataFrame({'auc':[auc]}), os.path.join(output_dir,'cancel_model_metrics.csv'), index=False)
    joblib.dump(model, os.path.join(output_dir,'cancel_model.joblib'))
    return auc

if __name__ == '__main__':
    run_cancel_model('../outputs/transactions_cleaned.csv','../outputs')
