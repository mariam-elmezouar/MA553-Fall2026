# Lab 7 — Judges, Agreement, and Rankings

**Session 8**

**Before the lab.** In this folder, run once:

```
pip install pandas pyarrow scikit-learn scipy
```

No download is needed. The votes are in the folder `data/`.

---

## The situation

MT-Bench asked 6 chat models the same 80 questions. People and GPT-4 then compared the
answers in pairs: for each pair, the judge chose answer A, answer B, or a tie. In this lab
you measure how often the judges agree, and you turn the votes into a ranking of the
models.

## The lab has two parts

**Part A — agreement between judges.** Compute Cohen's kappa by hand for two people and
for GPT-4 against a person, and count how often GPT-4 changed its winner when the order of
the answers changed.

**Part B — from votes to a ranking.** Compute win rates, fit the Bradley–Terry model as a
logistic regression, check whether two close models can be ordered with a bootstrap, and
use power to judge the size of a benchmark.

## Writing code

Six cells are marked **Write this yourself**: A2, A3, A4, B1, B2 and B3. Each gives the
goal, the variables to create, and the output to expect. The variable names matter,
because later cells use them. Everything else is written for you.

Everything is in `lab7.ipynb`. Work in the notebook.

## Running time

Every cell runs in a few seconds, except the bootstrap in B3, which takes about one
minute.

## The files in this folder

| File | What it is |
|---|---|
| `lab7.ipynb` | the lab |
| `data/human_votes.parquet` | 3,355 votes by people |
| `data/gpt4_votes.parquet` | 2,400 votes by GPT-4 |

The votes come from Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot
Arena*, released as `lmsys/mt_bench_human_judgments` on Hugging Face.

## What to hand in

Submit your completed notebook through Moodle.
