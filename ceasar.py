def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (Enter 'e' for encrypt, 'd' for decrypt, 'q' to quit): ").lower().strip()
        
        if choice not in ['e', 'd', 'q']:
            print("Invalid choice. Please try again.")
            continue
            
        if choice == 'q':
            print("Exiting the program. Goodbye!")
            break

        text = input("Enter the text: ").strip()
        
        shift = get_integer_input("Enter the shift value: ")
        
        if choice == 'e':
            print(f"Encrypted text: {encrypt(text, shift)}")
        else:
            print(f"Decrypted text: {decrypt(text, shift)}")

        another_round = input("Do you want to go again? (y/n): ").lower().strip()
        if another_round != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
