import csv
import os

def read_csv_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            print(f"Headers: {', '.join(headers)}")
            print("-" * 50)
            
            rows = []
            for row in csv_reader:
                rows.append(row)
                print(row)
            
            print("-" * 50)
            print(f"Total rows read: {len(rows)}")
            return rows
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def read_csv_as_dict(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            rows = []
            for row in csv_reader:
                rows.append(row)
                print(row)
            
            print("-" * 50)
            print(f"Total rows read: {len(rows)}")
            return rows
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def main():
    print("CSV File Reader")
    print("=" * 50)
    filename = input("Enter the CSV filename: ")
    
    print("\nChoose reading method:")
    print("1. Read as list (default)")
    print("2. Read as dictionary")
    choice = input("Enter choice (1 or 2): ").strip()
    
    print("\n")
    if choice == "2":
        read_csv_as_dict(filename)
    else:
        read_csv_file(filename)

if __name__ == "__main__":
    main()
