# Lab 0 — Does the number hold up?

**Session 1**

**If your own setup will not work:** go to colab.research.google.com, choose
File > Upload notebook, and upload `lab0.ipynb` from this folder. Everything
the lab needs is already installed there.

---

## The situation

`result_card.md` in this folder reports a result: one method beats another
by 3.5 percentage points on a medical classification task. The code that
produced it is here too, and it runs in seconds.

Your job is to find out how much that number is worth.

## The lab has two parts

**Part A — how the result was made.** The whole procedure, one step at a
time: what the data is, why some patients are held back, how a model is
trained, and what accuracy means. No prior machine learning is assumed. If
you have done this before, it will take you ten minutes.

**Part B — does the number hold up?** You predict what happens when one
thing changes, run it, and see how far off you were. Then you repeat the
comparison with both methods given the same effort, and write a claim you
can defend.

Everything is in `lab0.ipynb`. Work in the notebook — it has the cells for
your predictions and your written answers.

## Before you start

From the top folder of this repository:

```bash
python check_setup.py
```

If that passes, start Jupyter and open `lab0/lab0.ipynb`:

```bash
jupyter notebook
```

## A note on the numbers

You may not get exactly 3.5 percentage points. Software libraries change,
and small differences are normal. **If your number differs, write down what
you got and by how much.** That is a real observation about how fragile a
published number can be, and it belongs in your write-up rather than being
tidied away.

## What to hand in

Submit your completed notebook through Moodle. It must contain:

1. Your prediction, and the reasoning behind it.
2. The results you got, with all runs shown.
3. An explanation of any difference between your prediction and the result.
4. One claim you are prepared to defend in class.
5. One limitation of that claim.

Restart the kernel and run every cell from top to bottom before you submit.

You may use an AI assistant. You must understand and be able to explain
every line you hand in, and you must add a short note saying what the
assistant produced and what you changed.
