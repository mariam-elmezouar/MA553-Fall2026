"""
monthly_report.py — total taxi charges by borough, October 2024 to March 2025.

This script was written by a colleague. It runs without error and prints a
table of charges by borough and a grand total. Part B of the lab asks you to
check whether the numbers are right.

Run it from the lab folder:

    python monthly_report.py

Or, from the notebook:

    from monthly_report import run_report
    report = run_report()
"""

from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent / "data"
ZONES = Path(__file__).resolve().parent / "taxi_zone_lookup_revised.csv"


def charges_by_borough(trips, zones):
    """Attach the borough to each trip and sum the charges per borough."""
    # Keep complete records only.
    trips = trips.dropna()
    # Refunds and reversals are not charges, so leave them out.
    trips = trips[trips["total_amount"] >= 0]
    with_borough = trips.merge(zones[["LocationID", "Borough"]],
                               left_on="PULocationID", right_on="LocationID",
                               how="left")
    return with_borough.groupby("Borough")["total_amount"].sum()


def run_report(verbose=True):
    zones = pd.read_csv(ZONES)
    totals = None
    for path in sorted(DATA.glob("yellow_tripdata_*.parquet")):
        month = charges_by_borough(pd.read_parquet(path), zones)
        totals = month if totals is None else totals.add(month, fill_value=0)
    totals = totals.sort_values(ascending=False)
    if verbose:
        print("Total charges by borough, October 2024 to March 2025\n")
        print(totals.map("{:>18,.2f}".format).to_string())
        print(f"\nGrand total: {totals.sum():,.2f}")
    return totals


if __name__ == "__main__":
    run_report()
