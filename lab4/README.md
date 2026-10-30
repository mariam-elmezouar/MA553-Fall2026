# Lab 4 — Intervals and Tests on the Frontier

**Session 5**

**Before the lab.** This lab uses the January 2025 file you downloaded for
Lab 2, at `../lab2/data/yellow_tripdata_2025-01.parquet`. If it is missing,
run `python get_data.py` in the `lab2` folder. No new packages are needed:
`scipy`, used for the t-test, is installed with scikit-learn. Run
`python check_setup.py` from the repository root if you are unsure.

---

## The situation

In Lab 3 you compared five model families on one test set of 100,000 trips,
and you chose a model under two budgets. Each comparison gave one number per
model. In this lab you measure how far those numbers could move, and you test
whether the differences between models are more than chance.

## The lab has two parts

**Part A — the methods.** The sampling distribution of a mean, a 95%
confidence interval and how often it contains the population mean, a
bootstrap interval for a test MAE, and the paired t-test and swap (permutation) test
for two models scored on the same trips.

**Part B — what the intervals and tests show.** An interval for the cost of
Budget 2 from Lab 3, the decision-tree-against-random-forest comparison on fewer test trips,
a t-test on cross-validation fold scores and why it is not valid, and one
limitation.

## Writing code

Six cells are marked **Write this yourself**: A2, A4, A5, B1, B2 and B3. Each
gives the goal, the variables to create, and the output to expect. The
variable names matter, because later cells use them. Everything else is
written for you.

Everything is in `lab4.ipynb`. Work in the notebook.

## Running time

- A1 fits four models on 1,000,000 trips. The random forest takes one to two
  minutes; run A1 once.
- B3 runs 5-fold cross-validation for two models on 100,000 trips, which
  takes about a minute.
- Results that use random draws vary slightly from run to run. The expected
  values in the notebook say "about" where this applies.

## The files in this folder

| File | What it is |
|---|---|
| `lab4.ipynb` | the lab |

The trip data are real, published by the NYC Taxi and Limousine Commission.

## What to hand in

Submit your completed notebook through Moodle by **Wednesday 4 November,
09:00**. It must contain:

1. The six **Write this yourself** cells, run, with their output.
2. Every **Answer here** cell filled in.

Restart the kernel and run every cell from top to bottom before submitting.
Do not submit the data file.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and add a short note saying what the assistant
produced and what you changed.
