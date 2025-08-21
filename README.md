# 📄 KRIV Data Analyst Project

A comprehensive data analysis project simulating a Data Analyst internship for KRIV Technologies, focusing on restaurant chain optimization through data-driven insights.

## 🎯 Project Overview

This project demonstrates end-to-end data analysis for a regional quick-service restaurant chain seeking to:
- **Improve sales performance**
- **Optimize menu items**
- **Reduce order cancellations**

The analysis uses synthetic POS transaction data with **250K+ rows** to showcase how data processing, analysis, and modeling generate actionable business insights.

## 📁 Project Structure

```
KRIV_Data_Analyst_Project/
├── data/                    # Raw transactional dataset
│   └── pos_transactions.csv
├── kriv_src/               # Python analysis scripts
│   ├── data_prep.py        # Data cleaning and preparation
│   ├── eda.py              # Exploratory data analysis
│   ├── clustering.py       # Customer segmentation
│   ├── cancel_model.py     # Cancellation prediction model
│   ├── forecasting.py      # Revenue forecasting
│   └── utils.py            # Utility functions
├── outputs/                # Generated reports and visualizations
│   ├── *.csv              # Analysis results
│   ├── *.png              # Charts and graphs
│   └── *.joblib           # Trained models
├── main.py                 # Pipeline orchestration
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🔄 Analysis Workflow

### Step 1: Data Preparation (`data_prep.py`)
- **Input**: Raw transactional data
- **Process**: 
  - Clean column names and data types
  - Handle missing values
  - Standardize menu categories
- **Output**: `transactions_cleaned.csv`

### Step 2: Exploratory Data Analysis (`eda.py`)
- **Key Metrics**:
  - Total orders and revenue
  - Cancellation percentage
  - Average order value
- **Insights**:
  - Top menu items by revenue
  - Cancellation patterns by delivery time
- **Outputs**: KPI summary, revenue charts, trend analysis

### Step 3: Customer Segmentation (`clustering.py`)
- **Features**: Average spend, order frequency, customer behavior
- **Method**: K-Means clustering
- **Segments**: Loyal vs. occasional customers
- **Output**: `customer_clusters.csv`

### Step 4: Cancellation Prediction (`cancel_model.py`)
- **Model**: Logistic Regression
- **Features**: Delivery time, order size, menu category
- **Metrics**: AUC score, classification report
- **Output**: Trained model and performance metrics

### Step 5: Revenue Forecasting (`forecasting.py`)
- **Method**: SARIMAX time series model
- **Input**: Daily revenue aggregation
- **Forecast**: Next 28 days of revenue
- **Output**: Forecast chart and predictions

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Data Processing** | Python, Pandas, NumPy | Data manipulation and analysis |
| **Visualization** | Matplotlib, Seaborn | Charts and graphs |
| **Machine Learning** | Scikit-learn | Clustering and prediction |
| **Time Series** | Statsmodels | Revenue forecasting |
| **Data Storage** | CSV files | Simulated database |

## 📊 Business Impact (Simulated Results)

| Metric | Improvement |
|--------|-------------|
| **High-margin product identification** | Targeted promotion strategy |
| **Cancellation reduction** | ~8% decrease through predictive modeling |
| **Demand forecasting** | Improved staffing and supply chain decisions |
| **Overall revenue uplift** | ~12% simulated improvement |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone or extract the repository**
   ```bash
   cd KRIV_Data_Analyst_Project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the analysis pipeline**
   ```bash
   python main.py
   ```

### Output Files

After running the pipeline, check the `outputs/` folder for:

**📈 Data Files:**
- `kpis_summary.csv` - Key performance indicators
- `customer_clusters.csv` - Customer segmentation results
- `weekly_revenue_forecast.csv` - Revenue predictions
- `cancel_model_metrics.csv` - Model performance metrics

**📊 Visualizations:**
- `top_menu_revenue.png` - Top-performing menu items
- `daily_revenue.png` - Revenue trends over time
- `revenue_forecast.png` - Future revenue projections

**🤖 Models:**
- `cancel_model.joblib` - Trained cancellation prediction model

## 📝 Notes

- This project uses **synthetic data** for demonstration purposes
- All business impact metrics are **simulated** for educational value
- The analysis pipeline is designed to be **reproducible** and **scalable**
- Results can be extended to real-world restaurant data with minimal modifications

## 🤝 Contributing

This is a demonstration project, but suggestions for improvements are welcome!

## 📄 License

This project is for educational purposes as part of a simulated data analyst internship.