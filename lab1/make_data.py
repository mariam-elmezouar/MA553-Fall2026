"""Generates the Lab 2 dataset. Run once; the CSV is committed to the repo."""
import numpy as np, pandas as pd

rng = np.random.default_rng(553)

N_UNITS = 300
rows = []
unit_effect = rng.normal(0, 1.1, N_UNITS)          # persistent per-unit quirk
site_of_unit = rng.integers(0, 4, N_UNITS)

for u in range(N_UNITS):
    n_insp = rng.integers(3, 9)
    day = rng.integers(0, 120)
    age = rng.integers(6, 180)
    for _ in range(n_insp):
        day += rng.integers(20, 70)
        age += 1
        vibration = rng.normal(2.5, 0.8) + 0.35 * unit_effect[u]
        temperature = rng.normal(68, 9) + 0.5 * unit_effect[u]
        hours = rng.gamma(4, 120)
        inspector = rng.integers(0, 6)

        logit = (-3.1
                 + 0.85 * (vibration - 2.5)
                 + 0.0018 * (hours - 480)
                 + 0.009 * (age - 90)
                 + 1.05 * unit_effect[u])
        p = 1 / (1 + np.exp(-logit))
        failed = rng.random() < p

        rows.append(dict(
            unit_id=f"U{u:03d}",
            inspection_day=int(day),
            site=f"S{site_of_unit[u]}",
            inspector=f"I{inspector}",
            age_months=int(age),
            hours_since_service=round(float(hours), 1),
            vibration_mm_s=round(float(vibration), 3),
            temperature_c=round(float(temperature), 2),
            repair_cost_cad=round(float(rng.gamma(3, 700)), 2) if failed else 0.0,
            failed_within_30d=int(failed),
            **{f"sensor_{k:02d}": round(float(rng.normal(0, 1)), 3) for k in range(1, 41)},
        ))

df = pd.DataFrame(rows).sort_values("inspection_day").reset_index(drop=True)

# missing temperatures (sensor outages)
miss = rng.random(len(df)) < 0.07
df.loc[miss, "temperature_c"] = np.nan

# duplicated records (same inspection entered twice)
dup_idx = rng.choice(len(df), size=int(0.08 * len(df)), replace=False)
df = pd.concat([df, df.iloc[dup_idx]], ignore_index=True)
df = df.sample(frac=1, random_state=7).reset_index(drop=True)

df.to_csv("inspections.csv", index=False)
print(df.shape, "failure rate:", round(df.failed_within_30d.mean(), 3),
      "units:", df.unit_id.nunique(), "dups:", len(dup_idx))
