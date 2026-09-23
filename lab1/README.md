# Lab 1 — Model Evaluation and Data Leakage

**Session 2**

**If your own setup will not work:** go to colab.research.google.com, choose
File > Upload notebook, upload `lab1.ipynb`, and upload `inspections.csv`
alongside it.

---

## The situation

A model has been built to predict equipment failure from routine inspection
readings. It reports an AUC of almost 1.0 on data held out from training.

That score is not credible. Your task is to determine why, and to produce an
estimate that can be defended.

## The lab has two parts

**Part A — cross-validation and pipelines.** Rotating which part of the data
is used for evaluation instead of relying on a single split, and packaging
the preprocessing steps together with the model so they cannot use the
evaluation rows. No prior experience is assumed.

**Part B — the audit.** Five separate faults inflate the reported score.
Each requires its own correction, and one of the five is not in the data at
all.

## Writing code

Five cells are marked **Write this yourself**: A2, A5, B4, B5 and B6. Each
gives the goal, the variables to create, and the output to expect, so you
can check your own work. The variable names matter, because later cells use
them. Everything else is written for you.

Everything is in `lab1.ipynb`. Work in the notebook.

## The data

`inspections.csv` — 1,712 inspection records covering 300 pieces of
equipment over about two years. Each row is one inspection. The target
outcome is whether that unit failed within thirty days.

The data are generated rather than real. `make_data.py` is the generator,
included so you can see exactly what was put in. Do not read it before
finishing Part B; it gives away the answers.

## What to hand in

Submit your completed notebook through Moodle. It must contain:

1. Your prediction from B1, and the reasoning behind it.
2. Your ranking of the five faults from B2, and the comparison in B8 between
   that ranking and what you measured.
3. The completed table from B8 — each fault, its correction, and the AUC
   before and after.
4. Your final estimate, produced with an appropriate way of dividing the
   data and a fitted pipeline, with a sentence saying why that division
   suits this prediction task.
5. One claim you are prepared to defend next week, and one thing that claim
   does not establish.

Restart the kernel and run every cell from top to bottom before submitting.
The slow cell at the end of B7 should be run outside class.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and add a short note saying what the assistant
produced and what you changed.
