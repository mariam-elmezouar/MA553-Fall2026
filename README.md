# MA553 — Statistical Learning and Data Science

Course repository for MA553, Fall 2026, Royal Military College of Canada.
Wednesdays 09:00–11:50, Girouard 332.

Everything you need for the labs is here: the Python environment, the lab
folders, and the data. Materials are added as the term goes on, so run
`git pull` before each class.

---

## What to do before the first class

You need Python and a few libraries. Follow whichever route suits you.

### Route 1 — conda (recommended)

```bash
git clone <REPO-URL>
cd ma553
conda env create -f environment.yml
conda activate ma553
python check_setup.py
```

### Route 2 — pip and a virtual environment

```bash
git clone <REPO-URL>
cd ma553
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python check_setup.py
```

### Route 3 — Google Colab (no installation)

If neither route above works, open the lab notebook in Colab. Everything is
already installed there. The link is at the top of each lab's README.

Use this if you are stuck. Do not spend an hour fighting your laptop the
night before class.

---

## Checking that it worked

`python check_setup.py` prints a short report. The last line tells you
whether you are ready:

```
ALL CHECKS PASSED — you are ready for class.
```

If a check fails, the script says which library is missing and how to
install it. Bring the error message to class if you cannot resolve it; a
broken environment is a normal thing to debug together, not something to be
embarrassed about.

---

## Folder layout

```
ma553/
├── README.md            this file
├── environment.yml      conda environment
├── requirements.txt     pip requirements
├── check_setup.py       run this to test your installation
└── lab0/                Session 1 lab
```

One folder is added per lab. Each has its own README explaining what to do.

---

## Submitting work

Submit through Moodle, not through this repository. You do not need push
access here; you only ever pull.

Your submission must run from a clean environment. Before submitting,
restart the kernel and run every cell from top to bottom. Code that does not
execute is not marked.

---

## Getting help

Bring problems to class, or email <mariam.el-mezouar@rmc.ca>. When you email
about an error, paste the full error message and say which route above you
used.
