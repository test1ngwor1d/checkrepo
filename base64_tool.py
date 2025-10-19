#!/usr/bin/env python3
"""
Base64 Encoder/Decoder Tool

This script provides functionality to encode and decode Base64 strings.
Base64 is a binary-to-text encoding scheme that represents binary data 
in an ASCII string format.
"""

import base64
import sys


def encode_to_base64(text):
    """
    Encode a string to Base64.
    
    Args:
        text (str): The text to encode
        
    Returns:
        str: Base64 encoded string
    """
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


def decode_from_base64(base64_string):
    """
    Decode a Base64 string.
    
    Args:
        base64_string (str): The Base64 encoded string to decode
        
    Returns:
        str: Decoded string
    """
    try:
        base64_bytes = base64_string.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        text = text_bytes.decode('utf-8')
        return text
    except Exception as e:
        return f"Error decoding: {str(e)}"


def encode_file_to_base64(file_path):
    """
    Encode a file's contents to Base64.
    
    Args:
        file_path (str): Path to the file to encode
        
    Returns:
        str: Base64 encoded string of file contents
    """
    try:
        with open(file_path, 'rb') as file:
            file_bytes = file.read()
            base64_bytes = base64.b64encode(file_bytes)
            return base64_bytes.decode('utf-8')
    except Exception as e:
        return f"Error encoding file: {str(e)}"


def decode_base64_to_file(base64_string, output_path):
    """
    Decode a Base64 string and save to a file.
    
    Args:
        base64_string (str): The Base64 encoded string
        output_path (str): Path where to save the decoded file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        base64_bytes = base64_string.encode('utf-8')
        file_bytes = base64.b64decode(base64_bytes)
        with open(output_path, 'wb') as file:
            file.write(file_bytes)
        return True
    except Exception as e:
        print(f"Error decoding to file: {str(e)}")
        return False


def interactive_mode():
    """
    Run the tool in interactive mode.
    """
    print("=" * 50)
    print("Base64 Encoder/Decoder Tool")
    print("=" * 50)
    print("\nOptions:")
    print("1. Encode text to Base64")
    print("2. Decode Base64 to text")
    print("3. Encode file to Base64")
    print("4. Decode Base64 to file")
    print("5. Exit")
    print("=" * 50)
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            text = input("Enter text to encode: ")
            encoded = encode_to_base64(text)
            print(f"\nEncoded Base64: {encoded}")
            
        elif choice == '2':
            base64_string = input("Enter Base64 string to decode: ")
            decoded = decode_from_base64(base64_string)
            print(f"\nDecoded text: {decoded}")
            
        elif choice == '3':
            file_path = input("Enter file path to encode: ")
            encoded = encode_file_to_base64(file_path)
            print(f"\nEncoded Base64:\n{encoded}")
            
        elif choice == '4':
            base64_string = input("Enter Base64 string: ")
            output_path = input("Enter output file path: ")
            if decode_base64_to_file(base64_string, output_path):
                print(f"\nSuccessfully decoded to {output_path}")
            
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-5.")


def main():
    """
    Main function to handle command line arguments or run interactive mode.
    """
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 3:
        command = sys.argv[1].lower()
        data = sys.argv[2]
        
        if command == 'encode' or command == '-e':
            result = encode_to_base64(data)
            print(result)
        elif command == 'decode' or command == '-d':
            result = decode_from_base64(data)
            print(result)
        else:
            print("Usage:")
            print("  Interactive mode: python base64_tool.py")
            print("  Encode: python base64_tool.py encode 'your text'")
            print("  Decode: python base64_tool.py decode 'base64string'")
    else:
        print("Usage:")
        print("  Interactive mode: python base64_tool.py")
        print("  Encode: python base64_tool.py encode 'your text'")
        print("  Decode: python base64_tool.py decode 'base64string'")


if __name__ == "__main__":
    main()
