"""
CSV File Reader Examples

This script demonstrates two approaches for reading CSV files in Python:
1. Using Python's built-in csv module
2. Using the pandas library

Author: Created for test1ngwor1d/checkrepo
"""

import csv
import os


def read_csv_with_builtin(file_path):
    """
    Read a CSV file using Python's built-in csv module.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of rows from the CSV file
    """
    rows = []
    
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            header = next(csv_reader, None)
            if header:
                print(f"Header: {header}")
                rows.append(header)
            
            for row in csv_reader:
                rows.append(row)
                print(f"Row: {row}")
        
        print(f"\nTotal rows read: {len(rows)}")
        return rows
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


def read_csv_with_dict_reader(file_path):
    """
    Read a CSV file using csv.DictReader for dictionary-based access.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: List of dictionaries representing rows
    """
    rows = []
    
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            print(f"Column names: {csv_reader.fieldnames}")
            
            for row in csv_reader:
                rows.append(row)
                print(f"Row as dict: {row}")
        
        print(f"\nTotal rows read: {len(rows)}")
        return rows
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


def read_csv_with_pandas(file_path):
    """
    Read a CSV file using pandas library.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        DataFrame: Pandas DataFrame containing the CSV data
    """
    try:
        import pandas as pd
        
        df = pd.read_csv(file_path)
        
        print("DataFrame Info:")
        print(df.info())
        print("\nFirst few rows:")
        print(df.head())
        print(f"\nShape: {df.shape} (rows, columns)")
        
        return df
        
    except ImportError:
        print("Error: pandas library is not installed.")
        print("Install it using: pip install pandas")
        return None
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file with pandas: {e}")
        return None


def main():
    """
    Main function to demonstrate CSV reading methods.
    """
    print("=" * 60)
    print("CSV File Reader Examples")
    print("=" * 60)
    
    csv_file = "sample_data.csv"
    
    if not os.path.exists(csv_file):
        print(f"\nNote: '{csv_file}' does not exist.")
        print("Please provide a valid CSV file path to test these functions.\n")
        print("Example usage:")
        print("  rows = read_csv_with_builtin('your_file.csv')")
        print("  rows = read_csv_with_dict_reader('your_file.csv')")
        print("  df = read_csv_with_pandas('your_file.csv')")
        return
    
    print("\n" + "=" * 60)
    print("Method 1: Using csv.reader()")
    print("=" * 60)
    read_csv_with_builtin(csv_file)
    
    print("\n" + "=" * 60)
    print("Method 2: Using csv.DictReader()")
    print("=" * 60)
    read_csv_with_dict_reader(csv_file)
    
    print("\n" + "=" * 60)
    print("Method 3: Using pandas.read_csv()")
    print("=" * 60)
    read_csv_with_pandas(csv_file)


if __name__ == "__main__":
    main()
