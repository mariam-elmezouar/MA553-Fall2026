# Lab 3 — The Cost–Accuracy Frontier

**Session 4**

**Before the lab.** This lab uses the January 2025 file you downloaded for
Lab 2, at `../lab2/data/yellow_tripdata_2025-01.parquet`. If it is missing,
run `python get_data.py` in the `lab2` folder. No new packages are needed;
run `python check_setup.py` from the repository root if you are unsure.

---

## The situation

A taxi company wants to tell each passenger, at pickup, how many minutes the
trip will take. You will predict the trip duration from five features known
at pickup (distance, pickup hour, weekday, pickup zone, dropoff zone), using
the five model families from the session. For each model you measure what it
costs and how accurate it is, and then you choose a model for two different
uses.

## The lab has two parts

**Part A — fitting the five families.** The linear model, nearest neighbours,
a decision tree, a random forest and gradient boosting, each measured on the
same 100,000 test trips: time to fit, time to predict, test error and model
size. Then a learning curve and a small tree to read.

**Part B — auditing the result and choosing a model.** You check how the
linear model uses the pickup hour and correct it, give it combinations of
zones, build one table that compares every model, and choose a model under
two budgets.

## Writing code

Five cells are marked **Write this yourself**: A3, A4, B1, B2 and B3. Each
gives the goal, the variables to create, and the output to expect. The
variable names matter, because later cells use them. Everything else is
written for you.

Everything is in `lab3.ipynb`. Work in the notebook.

## Running time

- A4 and B3 fit models on 1,000,000 trips. The random forest takes one to two
  minutes; run it once and keep the result.
- Nearest neighbours is measured on 10,000 training trips only. Its predict
  time grows with the training size.
- Times depend on your machine. Compare models measured on the same machine.

## The files in this folder

| File | What it is |
|---|---|
| `lab3.ipynb` | the lab |

The trip data are real, published by the NYC Taxi and Limousine Commission.

## What to hand in

Submit your completed notebook through Moodle. It must contain:

1. The five **Write this yourself** cells, run, with their output.
2. Every **Answer here** cell filled in.
3. From B3: the frontier table.
4. From B4: your choice under each budget, with the numbers that decide it.
5. From B5: one limitation.

Restart the kernel and run every cell from top to bottom before submitting.
Do not submit the data file.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and add a short note saying what the assistant
produced and what you changed.
