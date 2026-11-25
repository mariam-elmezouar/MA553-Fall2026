# Session 9 — A Question-Answering Pipeline

**Session 9 workbook (done in class)**

## Before class

This workbook uses the two models you already downloaded:

| Model | Downloaded in | Expected folder |
|---|---|---|
| search model `all-MiniLM-L6-v2` | Lab 5 | `../lab5/model/all-MiniLM-L6-v2` |
| language model `Qwen2.5-1.5B-Instruct` | Lab 6 | `../lab6/model/qwen2.5-1.5b-instruct` |

If a model is missing, run `python get_data.py` in that lab's folder first. If your
models are in another place, change the two paths in the first code cell.

The questions (`squad-dev-v1.1.json`, about 5 MB) are in this folder. No download is
needed.

---

## How the session works

The slides and the notebook alternate. After each block of slides, work through the
matching part of `session9.ipynb`.

| Part | What you measure | Running time |
|---|---|---|
| 1 | how often search finds the right paragraph | about 1 minute |
| 2 | accuracy of each step, and where the errors come from | 2 to 4 minutes |
| 3 | time and prompt length against accuracy | 3 to 5 minutes |
| 4 | what changes when questions move to new topics | about 2 minutes |

Four cells are marked **Write this yourself**. They are short.

## The data

SQuAD (Stanford Question Answering Dataset), development set version 1.1: questions about
Wikipedia paragraphs, each with a known answer.

## What to hand in

Submit your completed notebook through Moodle at the end of the session.
