import argparse
import csv


def open_source(filename):
    with open(filename) as fh:
        reader = csv.DictReader(fh)
        return list(reader)


def write_source(filename, selected_columns, rows):
    with open(filename, 'w', newline='') as wfh:
        writer = csv.DictWriter(wfh, fieldnames=selected_columns)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        prog="csv_column_selector",
        description="Select specific columns from a CSV file."
    )
    parser.add_argument("--source", help="Source filename for reading")
    parser.add_argument("--target", help="Target filename for writing")
    parser.add_argument("--columns", nargs="+", help="Column names to select")
    args = parser.parse_args()

    rows = open_source(args.source)
    selected_rows = []
    for row in rows:
        selected_row = {column: row[column] for column in args.columns}
        selected_rows.append(selected_row)

    write_source(args.target, args.columns, selected_rows)
    print(f"Selected columns {args.columns} written to {args.target}")


if __name__ == "__main__":
    main()
