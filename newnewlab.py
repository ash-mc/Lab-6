def menu(): #string of menu that lists the different options available
    print("\nMenu"'\n-------------''\n1. Encode''\n2. Decode' '\n3. Quit')


def main():  # defining the main function menu of each option
    menu()

    numcon = True
    while numcon:
        choice = int(input("\nPlease enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored! ")
            menu()

        elif choice == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass} and the original password is {decoded_pass}")
            menu()

        elif choice == 3: #three choices, 1st encodes user input, 2nd decodes password from 1st, and 3rd quits program
            numcon = False


def encode(password):
    encodenum = ""
    for num in password:
        encodenum = encodenum + str((int(num) + 3) % 10)
        return encodenum


def decode(password): #done by partner Aleli, returns string of decoded password which is the same as the original
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