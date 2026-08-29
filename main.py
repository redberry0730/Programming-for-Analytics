import requests
import zipfile
import os

r = requests.get("https://github.com/pimatskku/sturdy-memory/raw/refs/heads/main/dataset.zip")

open("dataset.zip", "wb").write(r.content)

with zipfile.ZipFile("dataset.zip", "r") as zip_ref:
    zip_ref.extractall("data")

os.remove("dataset.zip")

print("Succesfully executed!")