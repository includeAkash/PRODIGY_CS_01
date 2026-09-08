def encrypt(message, shift):
    encrypted = ""

    for char in message:
        if char.isalpha():

            if char.isupper():
                new_ascii = ord(char) + shift

                while new_ascii > ord('Z'):
                    new_ascii -= 26

                encrypted += chr(new_ascii)

            else:
                new_ascii = ord(char) + shift

                while new_ascii > ord('z'):
                    new_ascii -= 26

                encrypted += chr(new_ascii)

        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:
        if char.isalpha():

            if char.isupper():
                new_ascii = ord(char) - shift

                while new_ascii < ord('A'):
                    new_ascii += 26

                decrypted += chr(new_ascii)

            else:
                new_ascii = ord(char) - shift

                while new_ascii < ord('a'):
                    new_ascii += 26

                decrypted += chr(new_ascii)

        else:
            decrypted += char

    return decrypted


print("===== Caesar Cipher Program =====")

while True:

    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))

        result = encrypt(message, shift)

        print("\nEncrypted Message:")
        print(result)

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))

        result = decrypt(message, shift)

        print("\nDecrypted Message:")
        print(result)

    elif choice == "3":
        print("Thank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice. Try again.")