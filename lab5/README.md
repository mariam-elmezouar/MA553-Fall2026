# Lab 5 — Searching Quora Questions

**Session 6**

**Before the lab.** Lab 5 needs two new libraries, `sentence-transformers` and
`faiss-cpu`, and data that are not in the repository. Do the steps for your
route once, before class.

*Conda (recommended).* From the top folder of the repository:

```
git pull
conda activate ma553
conda env update -f environment.yml
python check_setup.py
cd lab5
python get_data.py
```

*Pip and a virtual environment.* Activate your `.venv` first, then from the top
folder of the repository:

```
git pull
pip install -r requirements.txt
python check_setup.py
cd lab5
python get_data.py
```

*Google Colab.* First choose Runtime > Change runtime type > GPU. Do this
before anything else, because changing the runtime later deletes uploaded files.
With a GPU, the embedding step (A2) takes a few minutes instead of up to an
hour. Then upload `lab5.ipynb` and `get_data.py`, and in a new first cell run:

```
!pip install faiss-cpu
!python get_data.py
```

`get_data.py` downloads about 520,000 Quora questions and a small embedding
model (about 105 MB in total) into `data/` and `model/`. `check_setup.py`
should end with `ALL CHECKS PASSED`.

---

## The situation

In the session, we searched a large collection of questions for the ones that
ask the same thing as a query. In this lab you build that search yourself and
measure how well it works.

## The lab has two parts

**Part A — build and measure the search.** Embed the questions, try the
search, compute cosine similarity by hand, and measure recall at 10 with a
bootstrap interval.

**Part B — what the measurement shows.** Compare the search with keyword
search, with shorter vectors and with different numbers of groups searched in
an approximate index. Then read questions that ask the same thing as a query
but are not marked, and think about what the model has already seen.

## Writing code

Six cells are marked **Write this yourself**: A4, A5, A6, B1, B2 and B3. Each
gives the goal, the variables to create, and the output to expect. The variable
names matter, because later cells use them. Everything else is written for you.

Everything is in `lab5.ipynb`. Work in the notebook.

## Running time

- A2 embeds all the questions once and saves them in `vectors.npy`. This takes
  up to about an hour on a laptop without a GPU, and a few minutes with a GPU.
  Start it early. Later runs load the saved vectors in seconds.
- B1 (keyword search) and B3 (the index) take one to two minutes each.
- Times per query in B3 depend on your machine. Recall does not.

## The files in this folder

| File | What it is |
|---|---|
| `lab5.ipynb` | the lab |
| `get_data.py` | downloads the questions and the model |

The questions come from the Quora duplicate-questions set, as distributed in
the BEIR retrieval benchmark.

## What to hand in

Submit your completed notebook through Moodle by **Tuesday 10 November,
17:00**.
