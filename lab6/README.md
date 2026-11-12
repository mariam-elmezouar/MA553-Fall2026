# Lab 6 — Reading a Language Model's Probabilities

**Session 7**

**Before the lab.** In this folder, run once:

```
pip install torch transformers scipy matplotlib
python get_data.py
```

This downloads the SST-2 movie-review sentences (about 7 MB) and the language
model from the session, Qwen2.5-1.5B-Instruct (about 3 GB), into `data/` and
`model/`.

---

## The situation

In the session, we used a language model to label movie-review sentences as
positive or negative, and we found that its confidence was too high. In this
lab you repeat these measurements on 300 sentences, and you correct the
confidence.

## The lab has two parts

**Part A — inside the model.** Look at tokens, compute next-token
probabilities with softmax, change the temperature, and measure the model's
accuracy on the 300 sentences.

**Part B — can the probabilities be trusted?** Build the calibration table,
correct the confidence with temperature scaling, and measure what changes when
one word of the instruction changes.

## Writing code

Six cells are marked **Write this yourself**: A2, A3, A4, B1, B2 and B3. Each
gives the goal, the variables to create, and the output to expect. The variable
names matter, because later cells use them. Everything else is written for you.

Everything is in `lab6.ipynb`. Work in the notebook.

## Running time

- Loading the model takes about 30 seconds.
- Labelling the 300 sentences takes about 2 to 5 minutes on a laptop. It is
  done twice: once before A4 and once in B3. The results are saved, so the
  second run of the notebook is fast.
- Sampling answers in Part A takes one to two minutes.

## The files in this folder

| File | What it is |
|---|---|
| `lab6.ipynb` | the lab |
| `get_data.py` | downloads the sentences and the model |

The sentences come from SST-2 (Stanford Sentiment Treebank), as distributed in
the GLUE benchmark.

## What to hand in

Submit your completed notebook through Moodle.
