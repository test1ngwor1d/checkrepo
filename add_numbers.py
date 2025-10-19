import csv

def add_three_numbers_from_csv(csv_file):
    """
    Reads a CSV file and adds 3 numbers from it.
    
    Args:
        csv_file: Path to the CSV file containing numbers
        
    Returns:
        The sum of the three numbers
    """
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            
            header = next(csv_reader, None)
            
            row = next(csv_reader, None)
            
            if row is None or len(row) < 3:
                raise ValueError("CSV file must contain at least 3 numbers")
            
            num1 = float(row[0])
            num2 = float(row[1])
            num3 = float(row[2])
            
            total = num1 + num2 + num3
            
            print(f"Number 1: {num1}")
            print(f"Number 2: {num2}")
            print(f"Number 3: {num3}")
            print(f"Sum: {total}")
            
            return total
            
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    csv_filename = "numbers.csv"
    result = add_three_numbers_from_csv(csv_filename)
    
    if result is not None:
        print(f"\nThe sum of the three numbers is: {result}")
