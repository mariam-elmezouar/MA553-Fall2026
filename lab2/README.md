# Lab 2 — Data as a System

**Session 3**

**Before the lab, two things.** First, this lab needs one package the
September setup did not include: run `pip install pyarrow` (or
`conda install pyarrow`) in your course environment, then
`python check_setup.py` from the repository root. Second, run
`python get_data.py` in this folder. It downloads six
monthly files of New York taxi trips (October 2024 to March 2025) and the
city's zone table into `data/`, about 350 MB. Files already present are
skipped, so run it again if a download is interrupted.

**If your own setup will not work:** the files are too large for Colab's
upload. Use a lab machine, or ask before class.

---

## The situation

A colleague's script, `monthly_report.py`, computes total taxi charges by
borough for six months and prints a grand total. It runs without error. The
number is wrong. Your task is to find out why and to produce a figure that
can be defended.

## The lab has two parts

**Part A — reading and processing the files.** Reading only the columns a
calculation needs, processing one monthly file at a time, combining the
per-file results, and checking the file structure before using it. No prior
experience with Parquet or large files is assumed.

**Part B — the audit.** Five faults in the script each move the total. Each
one corresponds to a problem from the lecture, each can be caught by a check,
and each needs its own correction.

## Writing code

Five cells are marked **Write this yourself**: A2, A4, A5, B5 and B7. Each
gives the goal, the variables to create, and the output to expect. The
variable names matter, because later cells use them. Everything else is
written for you.

Everything is in `lab2.ipynb`. Work in the notebook.

## The files in this folder

| File | What it is |
|---|---|
| `lab2.ipynb` | the lab |
| `get_data.py` | downloads the data into `data/` |
| `monthly_report.py` | the script you are auditing; read it before running it |
| `taxi_zone_lookup_revised.csv` | the zone table the script uses; `data/taxi_zone_lookup.csv` is the city's version |

The trip data are real, published by the NYC Taxi and Limousine Commission.
The script and the revised zone table were written for this lab.

## What to hand in

Submit your completed notebook through Moodle. It must contain:

1. Your prediction from B1.
2. Every **Answer here** cell filled in.
3. The completed correction table from B8: each fault, the lecture problem it
   corresponds to, the check that catches it, and its effect on the January
   total.
4. From B9: the corrected six-month total by borough with the definition it
   answers, one conclusion, and one limitation.

Restart the kernel and run every cell from top to bottom before submitting.
A2 and A4 each take a few minutes. Do not submit the `data/` folder or
`data/january.csv`.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and add a short note saying what the assistant
produced and what you changed.
