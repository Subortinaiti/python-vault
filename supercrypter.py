import os

def encrypt_file(filename, password, goalfile):
    try:
        with open(filename, 'rb') as file:
            original_data = file.read()

        encrypted_data = bytearray()
        password_bytes = password.encode('utf-8')
        password_length = len(password_bytes)

        for i, byte in enumerate(original_data):
            encrypted_byte = byte ^ password_bytes[i % password_length]
            encrypted_data.append(encrypted_byte)

        with open(goalfile, 'wb') as output_file:
            output_file.write(encrypted_data)

        print(f"{filename} has been encrypted and saved as {goalfile}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def decrypt_file(filename, password, goalfile):
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = bytearray()
        password_bytes = password.encode('utf-8')
        password_length = len(password_bytes)

        for i, byte in enumerate(encrypted_data):
            decrypted_byte = byte ^ password_bytes[i % password_length]
            decrypted_data.append(decrypted_byte)

        with open(goalfile, 'wb') as output_file:
            output_file.write(decrypted_data)

        print(f"{filename} has been decrypted and saved as {goalfile}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



def encrypt_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if not filename.endswith(".encrypted"):
                file_path = os.path.join(root, filename)
                encrypted_file_path = os.path.join(root, f"{filename}.encrypted")
                encrypt_file(file_path, password, encrypted_file_path)
                os.remove(file_path)

def decrypt_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".encrypted"):
                file_path = os.path.join(root, filename)
                decrypted_file_path = os.path.join(root, filename[:-9])  # Remove the ".encrypted" extension
                decrypt_file(file_path, password, decrypted_file_path)
                os.remove(file_path)


def help_command():
    print("Available commands:")
    print("help           > show this list")
    print("exit/quit      > exit the program")
    print("enc [password] > encrypts the contents of the vault.")
    print("dec [password] > decrypts the contents of the vault.")


def main():
    while True:
        command = input("enc|dec [pw] > ").strip().split(" ")
        if not command:
            print("Invalid Syntax. type 'help' for a list of commands.")
        if command[0].lower() == "enc":
            if len(command) == 2:
                print("Are you sure you want to encrypt the vault with the password '"+command[1]+"'? this cannot be undone.")
                outcome = input("Y/N > ")
                if outcome.lower() in ["y","yes","true","siummus"]:
                    encrypt_folder("vault", command[1])
            else:
                print("Usage: enc [password]")
        elif command[0].lower() == "dec":
            if len(command) == 2:
                print("Are you sure you want to decrypt the vault with the password '"+command[1]+"'? this cannot be undone.")
                outcome = input("Y/N > ")
                if outcome.lower() in ["y","yes","true","siummus"]:
                    decrypt_folder("vault", command[1])
            else:
                print("Usage: dec [password]")
        elif command[0].lower() == "help":
            help_command()

        elif command[0].lower() in ["quit","exit"]:
            break
            
        else:
            print("Invalid Syntax. type 'help' for a list of commands.")




print("Supercrypter V. 1.0.1 is now running. type 'help' for a list of commands.")
main()
print("Program terminated.")





        









