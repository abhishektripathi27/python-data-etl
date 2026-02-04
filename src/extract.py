import csv

def extract_data(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
