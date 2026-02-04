from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def main():
    data = extract_data("data/input.csv")
    cleaned = transform_data(data)
    load_data(cleaned, "data/output.csv")

if __name__ == "__main__":
    main()
