# Base64 Encoder/Decoder Tool

A comprehensive Python tool for encoding and decoding Base64 strings and files.

## What is Base64?

Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. It's commonly used for:
- Encoding binary data in emails and URLs
- Storing complex data in text format
- Transmitting data over media designed for text
- Encoding credentials and tokens

## Features

- Encode text to Base64
- Decode Base64 to text
- Encode files to Base64
- Decode Base64 to files
- Interactive mode for easy use
- Command-line interface for automation

## Usage

### Interactive Mode

Run the script without arguments to enter interactive mode:

```bash
python3 base64_tool.py
```

You'll see a menu with options to encode/decode text and files.

### Command Line Mode

**Encode text:**
```bash
python3 base64_tool.py encode "Hello World"
# Output: SGVsbG8gV29ybGQ=
```

**Decode Base64:**
```bash
python3 base64_tool.py decode "SGVsbG8gV29ybGQ="
# Output: Hello World
```

## Examples

### Example 1: Encoding Text
```bash
$ python3 base64_tool.py encode "Python is awesome!"
UHl0aG9uIGlzIGF3ZXNvbWUh
```

### Example 2: Decoding Base64
```bash
$ python3 base64_tool.py decode "UHl0aG9uIGlzIGF3ZXNvbWUh"
Python is awesome!
```

### Example 3: Using Interactive Mode
```bash
$ python3 base64_tool.py
==================================================
Base64 Encoder/Decoder Tool
==================================================

Options:
1. Encode text to Base64
2. Decode Base64 to text
3. Encode file to Base64
4. Decode Base64 to file
5. Exit
==================================================

Enter your choice (1-5): 1
Enter text to encode: Hello World

Encoded Base64: SGVsbG8gV29ybGQ=
```

## How Base64 Works

Base64 encoding converts binary data into a set of 64 ASCII characters (A-Z, a-z, 0-9, +, /). The encoding process:

1. Takes 3 bytes (24 bits) of input data
2. Divides them into 4 groups of 6 bits each
3. Maps each 6-bit group to one of 64 ASCII characters
4. Uses '=' for padding when needed

For example:
- "Hello" → "SGVsbG8="
- The text is first converted to bytes
- Bytes are then encoded using the Base64 algorithm
- Result is a string that only uses safe ASCII characters

## Requirements

- Python 3.x (no external dependencies required)

## License

Free to use and modify.
