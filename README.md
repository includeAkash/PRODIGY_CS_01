# Caesar Cipher

A simple Python implementation of the Caesar Cipher encryption and decryption technique.

## Features

- Encrypt a message using a shift value.
- Decrypt an encrypted message using the same shift value.
- Preserves uppercase and lowercase letters.
- Keeps spaces, numbers, and special characters unchanged.
- Interactive menu with Encrypt, Decrypt, and Exit options.

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python caesar_cypher.py
```

## Usage

The program displays:

```text
===== Caesar Cipher Program =====

1. Encrypt
2. Decrypt
3. Exit
```

Choose an option and enter the message and shift value when prompted.

### Example

For encryption:

```text
Enter your choice: 1
Enter message: Hello World
Enter shift value: 3

Encrypted Message:
Khoor Zruog
```

To decrypt, use the same shift value:

```text
Enter your choice: 2
Enter encrypted message: Khoor Zruog
Enter shift value: 3

Decrypted Message:
Hello World
```

## How It Works

The Caesar Cipher shifts each alphabetic character by the specified number of positions.

For example, with a shift of 3:

- A → D
- B → E
- X → A
- Y → B
- Z → C

Uppercase and lowercase letters are handled separately, while non-alphabetic characters remain unchanged.

## Project Structure

```text
.
├── caesar_cypher.py
├── README.md
└── requirements.txt
```

## Notes

The program uses only Python's built-in functionality, so no third-party dependencies are needed.
