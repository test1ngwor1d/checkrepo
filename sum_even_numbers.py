#!/usr/bin/env python3
"""
Script to sum even numbers in even rows from a CSV file.
Even rows are considered as rows at indices 0, 2, 4, etc. (0-indexed)
or rows 2, 4, 6, etc. (1-indexed).
"""

import csv
import sys


def sum_even_numbers_in_even_rows(csv_file):
    """
    Read a CSV file and sum all even numbers that appear in even rows.
    
    Args:
        csv_file: Path to the CSV file
        
    Returns:
        int: Sum of all even numbers in even rows
    """
    total_sum = 0
    
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row_index, row in enumerate(csv_reader):
            if (row_index + 1) % 2 == 0:  # Even row in 1-indexed counting
                for value in row:
                    try:
                        num = int(value.strip())
                        if num % 2 == 0:
                            total_sum += num
                            print(f"Row {row_index + 1}: Found even number {num}")
                    except ValueError:
                        continue
    
    return total_sum


def main():
    if len(sys.argv) < 2:
        print("Usage: python sum_even_numbers.py <csv_file>")
        print("\nExample: python sum_even_numbers.py sample_data.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    try:
        result = sum_even_numbers_in_even_rows(csv_file)
        print(f"\n{'='*50}")
        print(f"Total sum of even numbers in even rows: {result}")
        print(f"{'='*50}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
