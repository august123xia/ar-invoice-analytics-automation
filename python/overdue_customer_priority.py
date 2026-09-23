from pathlib import Path

import pandas as pd


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def get_priority(amount):
    if amount >= 5000:
        return "High"
    elif amount >= 3000:
        return "Medium"
    else:
        return "Low"


def generate_customer_priority_summary():
    input_path = OUTPUT_DIR / "overdue_report.csv"

    df = pd.read_csv(input_path)

    customer_summary = (
        df
        .groupby("customer")["amount"]
        .sum()
        .reset_index()
        .rename(columns={"amount": "total_overdue"})
        .sort_values("total_overdue", ascending=False)
    )

    customer_summary["priority"] = customer_summary["total_overdue"].apply(get_priority)

    output_path = OUTPUT_DIR / "overdue_summary_by_customer.csv"
    customer_summary.to_csv(output_path, index=False)

    print("Customer overdue priority summary generated successfully.")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    generate_customer_priority_summary()