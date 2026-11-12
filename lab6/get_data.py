"""Download the data and the language model for Lab 6.

    pip install torch transformers scipy matplotlib
    python get_data.py

Creates, next to this script:
    data/SST-2/                    movie-review sentences labelled positive or negative
    model/qwen2.5-1.5b-instruct/   the language model from the session (about 3 GB)

Files that are already present are not downloaded again.
"""
import pathlib, urllib.request, zipfile

HERE = pathlib.Path(__file__).resolve().parent

# 1. The movie-review sentences (SST-2, from the GLUE benchmark)
data = HERE / "data"
data.mkdir(exist_ok=True)
if not (data / "SST-2" / "dev.tsv").exists():
    print("Downloading SST-2 (about 7 MB) ...")
    z = data / "SST-2.zip"
    urllib.request.urlretrieve("https://dl.fbaipublicfiles.com/glue/data/SST-2.zip", z)
    with zipfile.ZipFile(z) as f:
        f.extractall(data)
    z.unlink()
print("SST-2 files:", sorted(p.name for p in (data / "SST-2").iterdir()))

# 2. The language model
from huggingface_hub import snapshot_download
model_dir = HERE / "model" / "qwen2.5-1.5b-instruct"
print("Downloading Qwen2.5-1.5B-Instruct (about 3 GB) ...")
snapshot_download("Qwen/Qwen2.5-1.5B-Instruct", local_dir=model_dir)
print("Model saved in", model_dir)
