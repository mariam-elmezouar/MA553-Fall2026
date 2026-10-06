"""
Lab 2 — download the data.

Run this once, before the lab:

    python get_data.py

It downloads six months of New York City yellow taxi trip records and the
taxi zone lookup table into a folder called `data` beside this script.
About 350 MB in total. Files already present are skipped, so it is safe to
run again if a download is interrupted.

The data are published by the NYC Taxi and Limousine Commission at
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
"""

import sys
import urllib.request
from pathlib import Path

TRIPS = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{}.parquet"
ZONES = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

MONTHS = ["2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"]

DATA = Path(__file__).resolve().parent / "data"

# A file smaller than this is not a real download. It is usually an error
# page saved under the right name.
SMALLEST_SENSIBLE_TRIP_FILE = 1_000_000   # 1 MB
SMALLEST_SENSIBLE_ZONE_FILE = 1_000       # 1 KB


def size_text(path):
    """File size as a short string, in KB for small files."""
    n = path.stat().st_size
    return f"{n/1e3:6.0f} KB" if n < 1e6 else f"{n/1e6:6.1f} MB"


def fetch(url, target, smallest):
    """Download one file. Returns True if the file is present and sensible."""
    if target.exists() and target.stat().st_size >= smallest:
        print(f"  have   {target.name:38s} {size_text(target)}")
        return True

    print(f"  get    {target.name:38s} ...", end="", flush=True)
    partial = target.with_suffix(target.suffix + ".part")
    try:
        urllib.request.urlretrieve(url, partial)
    except Exception as error:
        print(f" failed: {error}")
        if partial.exists():
            partial.unlink()
        return False

    if partial.stat().st_size < smallest:
        print(f" failed: file is only {partial.stat().st_size} bytes")
        partial.unlink()
        return False

    partial.replace(target)
    print(f"\r  got    {target.name:38s} {size_text(target)}")
    return True


def main():
    DATA.mkdir(exist_ok=True)
    print(f"Downloading into {DATA}\n")

    results = []
    for month in MONTHS:
        target = DATA / f"yellow_tripdata_{month}.parquet"
        results.append(fetch(TRIPS.format(month), target,
                             SMALLEST_SENSIBLE_TRIP_FILE))

    results.append(fetch(ZONES, DATA / "taxi_zone_lookup.csv",
                         SMALLEST_SENSIBLE_ZONE_FILE))

    total = sum(f.stat().st_size for f in DATA.iterdir() if f.is_file()) / 1e6
    print(f"\n{sum(results)} of {len(results)} files present, "
          f"{total:.0f} MB in total.")

    if not all(results):
        print("\nSome downloads failed. Run this script again: files already "
              "downloaded are skipped.")
        print("If they keep failing, the files can be downloaded by hand from")
        print("https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page")
        print(f"and placed in {DATA}")
        sys.exit(1)

    print("\nReady. Open lab2.ipynb.")


if __name__ == "__main__":
    main()
