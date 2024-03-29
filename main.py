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

        elif choice == 3: #3 options, 1st encodes, 2nd decodes, 3rd quits
            numcon = False


def encode(password):
    encodenum = ""
    for num in password:
        encodenum = encodenum + str((int(num) + 3) % 10)
        return encodenum

def decode(password): # decode fucntion done by Aleli Vaca
    empty_str = ""
    for i in password:
        if i == "0":
            i = "7"
        if i == "1":
            i = "8"
        if i == "2":
            i = "9"
        else:
            i = int(i)
            i -= 3
            i = str(i)
        empty_str += i
    return empty_str



if __name__ == '__main__':
    main()
