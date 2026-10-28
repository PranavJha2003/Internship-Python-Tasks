
import csv
import json
from pathlib import Path


def clean_value(value):
    """Trim whitespace and convert empty values to None."""
    if value is None:
        return None

    value = value.strip()
    return value if value else None


def read_and_clean_csv(input_path):
    """Read a CSV file and return cleaned records."""
    records = []

    with open(input_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header.")

        for row in reader:
            cleaned_row = {}

            for key, value in row.items():
                if key is None:
                    raise ValueError("A CSV row contains extra columns.")

                cleaned_key = key.strip()
                cleaned_value = clean_value(value)
                cleaned_row[cleaned_key] = cleaned_value

            records.append(cleaned_row)

    return records


def write_json(records, output_path):
    """Write records to a JSON file."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)


def main():
    try:
        records = read_and_clean_csv("observations.csv")
        write_json(records, "output/observations.json")
        print(f"Successfully cleaned {len(records)} records.")

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
