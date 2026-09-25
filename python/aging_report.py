from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def get_aging_bucket(days):
    if days < 0:
        return "Not due"
    elif days <= 30:
        return "0-30 days"
    elif days <= 60:
        return "31-60 days"
    elif days <= 90:
        return "61-90 days"
    else:
        return "90+ days"


def generate_aging_reports():
    input_path = DATA_DIR / "invoices.csv"

    df = pd.read_csv(input_path)

    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["due_date"] = pd.to_datetime(df["due_date"])

    report_date = pd.to_datetime("2026-09-16")

    df["days_overdue"] = (report_date - df["due_date"]).dt.days
    df["aging_bucket"] = df["days_overdue"].apply(get_aging_bucket)

    aging_report = df
    unpaid_aging_report = df[df["status"] == "unpaid"]
    overdue_report = df[
        (df["status"] == "unpaid")
        & (df["days_overdue"] > 0)
    ].sort_values("days_overdue", ascending=False)

    overdue_summary_by_bucket = (
        overdue_report
        .groupby("aging_bucket")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    aging_report.to_csv(OUTPUT_DIR / "aging_report.csv", index=False)
    unpaid_aging_report.to_csv(OUTPUT_DIR / "unpaid_aging_report.csv", index=False)
    overdue_report.to_csv(OUTPUT_DIR / "overdue_report.csv", index=False)
    overdue_summary_by_bucket.to_csv(
        OUTPUT_DIR / "overdue_summary_by_bucket.csv",
        index=False
    )

    print("Aging reports generated successfully.")
    print("Output files:")
    print("- outputs/aging_report.csv")
    print("- outputs/unpaid_aging_report.csv")
    print("- outputs/overdue_report.csv")
    print("- outputs/overdue_summary_by_bucket.csv")


if __name__ == "__main__":
    generate_aging_report()