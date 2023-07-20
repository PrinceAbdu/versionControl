# Abdullah Alakashi
def decode(encoded_pass):
    decoded_pass = ''
    for digit in encoded_pass:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_pass += decoded_digit
    return decoded_pass


def main():
    while True:
        print("Menu")   #menu option
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")  #user input

        if option == "1":
            value = input("Please enter your password to encode: ")     #encoded password
            encoded_pass = encode(value)
            print("Your password has been encoded and stored!")
            print()
        elif option == "2":
            print("The encoded password is", encoded_pass, "and the original password is", decode(encoded_pass))
            #decoding password
        elif option == "3":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
