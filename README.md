# MA553 — Statistical Learning and Data Science

Course repository for MA553, Fall 2026, Royal Military College of Canada.
Wednesdays 09:00–11:50, Girouard 332.

Everything you need for the labs is here: the Python environment, the lab
folders, and the data. Materials are added as the term goes on, so run
`git pull` before each class. When the environment changes, the README of the
new lab says so; for lab 2 you need `pyarrow` (`pip install pyarrow` or
`conda install pyarrow`), and for lab 5 you need `sentence-transformers` and
`faiss-cpu` (see `lab5/README.md`). Then run `python check_setup.py` again.

---

## What to do before the first class

You need Python and a few libraries. Follow whichever route suits you.

### Route 1 — conda (recommended)

```bash
git clone https://github.com/mariam-elmezouar/MA553-Fall2026.git
cd MA553-Fall2026
conda env create -f environment.yml
conda activate ma553
python check_setup.py
```

### Route 2 — pip and a virtual environment

```bash
git clone https://github.com/mariam-elmezouar/MA553-Fall2026.git
cd MA553-Fall2026
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python check_setup.py
```

### Route 3 — Google Colab (no installation)

If neither route above works, go to colab.research.google.com, choose
File > Upload notebook, and upload the lab notebook from this repository.
Everything you need is already installed there.


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
MA553-Fall2026/
├── README.md            this file
├── environment.yml      conda environment
├── requirements.txt     pip requirements
├── check_setup.py       run this to test your installation
├── lab0/                Session 1 lab
├── lab1/                Session 2 lab
├── lab2/                Session 3 lab (run its get_data.py first; the data are not in the repo)
├── lab3/                Session 4 lab
├── lab4/                Session 5 lab
└── lab5/                Session 6 lab (new libraries; run its get_data.py first)
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
