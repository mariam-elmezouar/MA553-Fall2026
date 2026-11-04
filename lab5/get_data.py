"""Download the data and the embedding model for Lab 5.

    (with the ma553 environment active)
    python get_data.py

Creates, next to this script:
    data/quora/corpus.jsonl    about 523,000 Quora questions
    data/quora/queries.jsonl   15,000 query questions (10,000 of them have marked duplicates)
    data/quora/qrels/          which questions are marked duplicates of each query
    model/all-MiniLM-L6-v2/    a small sentence-embedding model (384 numbers per text)
"""
import pathlib, urllib.request, zipfile

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)

url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/quora.zip"
zip_path = DATA / "quora.zip"
if not (DATA / "quora" / "corpus.jsonl").exists():
    print("Downloading Quora (about 15 MB) ...")
    urllib.request.urlretrieve(url, zip_path)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(DATA)
    zip_path.unlink()
print("Quora files:", sorted(p.name for p in (DATA / "quora").iterdir()))

from sentence_transformers import SentenceTransformer
model_dir = HERE / "model" / "all-MiniLM-L6-v2"
if not model_dir.exists():
    print("Downloading the embedding model (about 90 MB) ...")
    SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2").save(str(model_dir))
print("Model saved in", model_dir)
