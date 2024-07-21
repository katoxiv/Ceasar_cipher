
# Caesar Cipher Script Documentation

## Overview
This script implements the Caesar Cipher encryption and decryption algorithm. It provides functionality to encrypt and decrypt text using a specified shift value, as well as a user-friendly interface for interactive use.

## Features
1. Encrypt text using a specified shift value
2. Decrypt text using a specified shift value
3. Interactive command-line interface for ease of use

## Usage
The script can be run from the command line with the following syntax:
```
python caesar_cipher.py
```

### Interactive Mode
Once the script is running, you will be presented with a menu:
1. Choose 'e' for encryption or 'd' for decryption
2. Enter the text to be processed
3. Enter the shift value (an integer)
4. View the result
5. Choose whether to continue or exit

### Examples
1. Encrypt a string:
   ```
   Do you want to encrypt or decrypt? (Enter 'e' for encrypt, 'd' for decrypt, 'q' to quit): e
   Enter the text: Hello, World!
   Enter the shift value: 3
   Encrypted text: Khoor, Zruog!
   ```

2. Decrypt a string:
   ```
   Do you want to encrypt or decrypt? (Enter 'e' for encrypt, 'd' for decrypt, 'q' to quit): d
   Enter the text: Khoor, Zruog!
   Enter the shift value: 3
   Decrypted text: Hello, World!
   ```

## Implementation Details

### Main Components
1. `encrypt(text: str, shift: int) -> str`: Function that performs the Caesar Cipher encryption on the input text.
2. `decrypt(text: str, shift: int) -> str`: Function that performs the Caesar Cipher decryption on the input text.
3. `get_integer_input(prompt: str) -> int`: Utility function to ensure valid integer input for the shift value.
4. `main() -> None`: Entry point of the script, handles the interactive mode and user input.

### Caesar Cipher Algorithm Implementation
The `encrypt()` function implements the Caesar Cipher algorithm as follows:
1. Iterate through each character in the input text.
2. If the character is a letter:
   a. Determine the base ASCII value ('A' for uppercase, 'a' for lowercase).
   b. Apply the shift: (ASCII value - base + shift) % 26 + base
   c. Convert the resulting ASCII value back to a character.
3. If the character is not a letter, leave it unchanged.
4. Return the resulting encrypted text.

The `decrypt()` function simply calls `encrypt()` with a negative shift value.

## Performance Considerations
- The script processes each character individually, which is efficient for the Caesar Cipher's simplicity.
- The modulo operation ensures that the shift wraps around the alphabet correctly.

## Limitations and Potential Improvements
- The current implementation only works with the 26 letters of the English alphabet.
- It does not handle different character sets or languages.
- The script could be extended to accept command-line arguments for non-interactive use.
- File input/output functionality could be added to process larger texts.

## Security Considerations
- The Caesar Cipher is a very simple encryption method and is not secure for sensitive information.
- It is vulnerable to frequency analysis and brute-force attacks.
- This implementation is for educational purposes only and should not be used for securing sensitive data.

## Dependencies
The script uses only Python standard library modules:
- `typing`: For type hinting (Python 3.5+)

No additional installations are required beyond a standard Python environment.