# Lab 0 — Does the number hold up?

**Session 1 · 9 September 2026**

**If your own setup will not work:** go to colab.research.google.com, choose
File > Upload notebook, and upload `lab0.ipynb` from this folder. Everything
the lab needs is already installed there.

---

## The situation

`result_card.md` reports a result: gradient boosting beats logistic
regression by 3.5 percentage points on a medical classification task. The
code that produced it is in this folder and it runs in seconds.

Your job is to find out how much that number is worth.

## What you will do

1. Run the released code and confirm you get the reported number.
2. Predict what happens when only the random split changes. Write the
   prediction down before running anything.
3. Run it again across many splits, and look at the spread.
4. Give the baseline the same tuning effort the proposed method received,
   and run it again.
5. Write a claim you can defend, and one thing it still does not establish.

The notebook `lab0.ipynb` walks you through all five steps. Work in the
notebook; it has the cells for your predictions and your written answers.

## Before you start

From the top of the repository:

```bash
python check_setup.py
```

If that passes, start Jupyter and open `lab0/lab0.ipynb`:

```bash
jupyter notebook
```

## A note on the numbers

You may not get exactly 3.5 percentage points. Library versions change, and
small differences are normal. **If your number differs, write down what you
got and by how much it differs.** That is a real observation about how
fragile a published number can be, and it belongs in your write-up rather
than being tidied away.

## What to submit

Submit your completed notebook through Moodle before the next session. It
must contain:

1. Your prediction, and the reasoning behind it.
2. The results you got, with all runs shown.
3. An explanation of any difference between the prediction and the result.
4. One claim you are prepared to defend in class next week.
5. One limitation of that claim.

Restart the kernel and run all cells from top to bottom before you submit.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and you must say in a short note what the assistant
produced and what you changed.
