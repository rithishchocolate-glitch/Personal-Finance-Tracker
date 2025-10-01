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
├── errors.log
