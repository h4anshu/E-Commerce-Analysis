📦 E-Commerce Data Analysis Project 📌 Overview

This project demonstrates a complete end-to-end analytics workflow for an e-commerce dataset. 
It covers:
**. Data ingestion:** CSV → MySQL database
**. Analysis:** Jupyter Notebook (Python, Pandas, SQLAlchemy)
**. Visualization:** Power BI dashboard

The goal is to uncover insights about orders, customers, sellers, products, payments, and logistics.

📂 Project Structure:

    ├── data/                     # Raw CSV files
    ├── ingestion_db.py           # ETL script (CSV → MySQL)
    ├── main.ipynb               # Jupyter notebook (analysis & KPIs)
    ├── e-commerce dashboard.pbix # Power BI dashboard
    └── README.md                 # Project documentation

**⚙️ Setup Instructions**

1. Requirements:
    . Python 3.8+
    . MySQL database
    . Power BI Desktop (for dashboard)

2. Install dependencies:
    pip install pandas sqlalchemy mysql-connector-python jupyter matplotlib

3. Database Setup
  . Create a MySQL database:
      CREATE DATABASE commerce;

  . Ingest Data into MySQL
         Place raw CSV files inside the data/ folder, then run:
         python ingestion_db.py

  This will load all CSVs as tables inside the commerce database.

4. Run Analysis Notebook
      This notebook connects to MySQL, runs queries, computes KPIs, and performs EDA.

5. Open Power BI Dashboard
      Open e-commerce dashboard.pbix in Power BI Desktop. Refresh the data connection to pull the latest analysis.

**📊 Key Insights**

    . Total Revenue (GMV): ~20M

    . Customers: ~98K

    . Orders: ~98K

    . Average Order Value (AOV): ~172

    . Top Categories: Electronics, Home & Furniture, Fashion

    . Payment Method: Credit cards dominate transactions

    . Regional Revenue: SP and RJ are top states

    . Delivery: Median ~10–12 days, some delays beyond SLA

**🚀 Future Improvements**

    . Automate ETL with Airflow/Prefect

    . Support incremental data loads

    . Build customer segmentation (RFM)

    . Add predictive models (LTV, churn, demand forecasting)

    . Cloud deployment for scalability

📜 License

This project is for educational and analytical purposes.
