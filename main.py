def menu():
    print("\nMenu"'\n-------------''\n1. Encode''\n2. Decode' '\n3. Quit')


def main():  # defining the main function menu of each option
    menu()

    numcon = True
    while numcon:
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored! ")
            menu()

        elif choice == 2:
            print(f"The encoded password is: ,  and the original password is:", password)
            menu()

        elif choice == 3:
            numcon = False


def encode(password):
    encodenum = ""
    for num in password:
        encodenum = encodenum + str((int(num) + 3) % 10)
        return encodenum


def decode(password):
    pass


# parthner does it


if __name__ == '__main__':
    main()
