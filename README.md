# Accounts Receivable Analytics & SOA Automation

[![Python Tests](https://github.com/august123xia/ar-invoice-analytics-automation/actions/workflows/python-tests.yml/badge.svg)](https://github.com/august123xia/ar-invoice-analytics-automation/actions/workflows/python-tests.yml)

## Project Overview

This project is an accounts receivable automation project using Python, Pandas, SQL, SQLite, and CSV files.

It processes invoice data, calculates overdue days, creates aging buckets, summarizes overdue balances by customer and aging category, and generates a structured statement of account summary.

The project is based on common finance operations workflows such as overdue invoice tracking, aging analysis, customer account review, dispute handling, unused credit review, unallocated payment handling, and statement of account preparation.

## Business Problem

Accounts receivable teams often need to manually track unpaid invoices, overdue balances, aging buckets, disputed invoices, unused credits, unallocated payments, and customer payment status.

Manual reporting can be time-consuming and error-prone, especially when multiple customers, overdue invoices, credits, and payments are involved.

This project automates part of the AR reporting process by generating structured overdue reports, customer-level summaries, aging bucket summaries, and statement of account outputs.

## Tech Stack

- Python
- Pandas
- SQL
- SQLite
- CSV
- Git / GitHub

## Key Features

- Read invoice data from CSV files
- Calculate days overdue based on invoice due dates
- Categorize invoices into aging buckets
- Filter unpaid and overdue invoices
- Generate overdue invoice reports
- Summarize overdue balances by customer
- Assign customer priority levels based on overdue amount
- Summarize overdue balances by aging bucket
- Generate a statement of account summary
- Separate undisputed invoices, disputed invoices, unused credits, and unallocated payments
- Calculate final payment request amount
- Validate reporting logic using SQL CTE queries

## Project Structure

```text
ar-invoice-analytics-automation/
├── README.md
├── data/
│   ├── invoices.csv
│   ├── soa_undisputed_invoices.csv
│   ├── soa_disputed_invoices.csv
│   ├── soa_unused_credits.csv
│   └── soa_unallocated_payments.csv
├── outputs/
│   ├── aging_report.csv
│   ├── unpaid_aging_report.csv
│   ├── overdue_report.csv
│   ├── overdue_summary_by_bucket.csv
│   ├── overdue_summary_by_customer.csv
│   └── customer_soa.txt
├── python/
│   ├── aging_report.py
│   ├── overdue_customer_priority.py
│   └── soa_generator.py
└── sql/
    ├── cte_customer_summary.sql
    └── cte_aging_bucket_summary.sql

```

## Sample Outputs

### Customer Overdue Summary

| Customer | Overdue Count | Total Overdue | Priority |
|---|---:|---:|---|
| Dnata | 1 | 5000 | High |
| Amazon | 1 | 3500 | Medium |
| Google | 1 | 1800 | Low |
| Ali | 1 | 800 | Low |

### Aging Bucket Summary

| Aging Bucket | Invoice Count | Total Amount |
|---|---:|---:|
| 90+ days | 1 | 5000 |
| 61-90 days | 1 | 3500 |
| 0-30 days | 2 | 2600 |

### Statement of Account Summary

| Item | Amount |
|---|---:|
| Total undisputed invoices | 4500 |
| Total disputed invoices | 1500 |
| Total unused credits | 800 |
| Total unallocated payments | 1400 |
| Payment request | 2300 |

## How to Run

Run the Python scripts from the project root directory:

```bash
python3 python/aging_report.py
python3 python/overdue_customer_priority.py
python3 python/soa_generator.py
```

Run the SQL validation scripts:

```bash
sqlite3 sql/ar_invoice.db < sql/cte_customer_summary.sql
sqlite3 sql/ar_invoice.db < sql/cte_aging_bucket_summary.sql
```


## Testing and CI

This project includes pytest tests for key business logic, including customer priority classification and aging bucket rules.

Tests can be run locally with:

```bash
pytest



## Python Modules

### aging_report.py

Generates invoice aging reports, unpaid aging reports, overdue invoice reports, and aging bucket summaries.

### overdue_customer_priority.py

Reads the overdue invoice report and generates customer-level overdue summaries with priority labels.

### soa_generator.py

Generates a structured statement of account summary by separating undisputed invoices, disputed invoices, unused credits, and unallocated payments.

The payment request is calculated as:

```text
Payment request = Total undisputed invoices - Total unused credits - Total unallocated payments
```

## SQL Validation

The SQL scripts use Common Table Expressions to validate the reporting logic.

### cte_customer_summary.sql

Creates a customer-level overdue summary using CTEs.

### cte_aging_bucket_summary.sql

Creates an aging bucket summary using CTEs.

## Future Improvements

- Add Streamlit dashboard
- Add FastAPI backend endpoints
- Store invoice data in PostgreSQL
- Add customer risk scoring
- Add email-ready SOA templates
- Add automated monthly AR reporting workflow
- Add unit tests for calculation logic

## Notes

All data used in this project is sample data created for demonstration purposes.