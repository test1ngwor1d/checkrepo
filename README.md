# CSV Even Number Sum Tool

This repository contains a Python script that sums even numbers from even rows in a CSV file.

## Files

- `sum_even_numbers.py` - Main script that processes CSV files
- `sample_data.csv` - Sample CSV file for testing

## Usage

```bash
python3 sum_even_numbers.py <csv_file>
```

### Example

```bash
python3 sum_even_numbers.py sample_data.csv
```

## How It Works

The script:
1. Reads a CSV file row by row
2. Identifies even rows (rows 2, 4, 6, etc. in 1-indexed counting)
3. Extracts all even numbers from those rows
4. Sums them up and displays the result

### Sample Output

For the included `sample_data.csv`:
```
Row 2: Found even number 6
Row 2: Found even number 8
Row 2: Found even number 10
Row 4: Found even number 16
Row 4: Found even number 18
Row 4: Found even number 20
Row 6: Found even number 26
Row 6: Found even number 28
Row 6: Found even number 30

==================================================
Total sum of even numbers in even rows: 162
==================================================
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)
