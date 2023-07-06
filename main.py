import random
import string
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, name):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'generated-passwords.txt')
    with open(file_path, 'a') as file:
        file.write("APPLICATION/SERVICE NAME: " + name + "\nGENERATED PASSWORD: " + password + '\n\n')

def main():
    print("WELCOME IN PASSWORD GENERATOR")
    print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))
    name = input("Enter the name of the application/service: ")
    length = int(input("Enter password length: "))
    print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))
    password = generate_password(length)
    print("Application/service name: \033[91m{}\033[00m".format(name))
    print("Generated password: \033[92m{}\033[00m".format(password))
    print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))
    save_password(password, name)
    print(f"The password has been saved in a .txt file on the desktop")
    print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))

if __name__ == '__main__':
    main()