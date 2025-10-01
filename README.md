## Personal Finance Tracker 💰

A Python + PostgreSQL + Power BI project to track **income, expenses, and balance** with automation and dashboards.

---

## 🚀 Features
- Add and view transactions using Python scripts
- Bulk load data from CSV files
- Store transactions in PostgreSQL
- Automate daily updates with Windows Task Scheduler
- Interactive Power BI dashboards:
  - Total Income, Total Expenses, Balance
  - Expenses by Category (Bar Chart)
  - Spending Trend over Time (Line Chart)
  - Date Range Filters (Slicers)

---

## 🛠 Tech Stack
- **Python** → Data ingestion & automation  
- **PostgreSQL** → Central database for storage  
- **Power BI** → Visualization & insights  
- **Task Scheduler** → Daily automation  

---

## 📂 Project Structure


```
Personal-Finance-Tracker/
│
├── add_transaction_pg.py         # Script to add income/expense records
├── advanced_summary.py            # Generate advanced summary reports
├── app_pg.py                      # Main entry point for the app
├── connect_db.py                  # Handles database connection
├── create_table.py                # Creates database tables
├── db_setup.py                    # Database setup script
├── insert_sample_data.py          # Insert sample transactions
├── load_csv_pg.py                 # Load data from CSV into PostgreSQL
├── main_finance.py                # Main finance tracker script
├── summary_pg.py                  # Generate summary reports
│
├── finance.db                     # Local SQLite DB (optional, dev use)
├── errors.log                     # Log file
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .gitignore                     # Ignore unnecessary files (venv, logs, etc.)
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Personal-Finance-Tracker.git
   cd Personal-Finance-Tracker
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Run `create_table.py` to create the necessary tables in PostgreSQL.
   - (Optional) Load sample data using:
     ```bash
     python insert_sample_data.py
     ```
     or
     ```bash
     python load_csv_pg.py
     ```

5. **Run the app**
   ```bash
   python main_finance.py
   ```


   ## ▶️ Usage

- **Add a transaction**
  ```bash
  python add_transaction_pg.py
  ```

- **Generate a summary**
  ```bash
  python summary_pg.py
  ```

- **Advanced summary**
  ```bash
  python advanced_summary.py
  ```

- **Bulk load from CSV**
  ```bash
  python load_csv_pg.py
  ```

- **Database setup**
  ```bash
  python db_setup.py
  ```

- **Power BI Dashboard**
  Open `dashboards/Finance_Tracker.pbix` in Power BI Desktop to view interactive reports.


