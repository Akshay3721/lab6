# Akshay Nandakumar

def encoder(number):
    number_list = [str(int(number[i]) + 3)[-1] for i in range(len(number))]
    return ''.join(number_list)


def decoder(password):
    stringify = ""
    for number in str(password):
        match number:
            case "0":
                stringify += "7"
            case "1":
                stringify += "8"
            case "2":
                stringify += "9"
            case "3":
                stringify += "0"
            case "4":
                stringify += "1"
            case "5":
                stringify += "2"
            case "6":
                stringify += "3"
            case "7":
                stringify += "4"
            case "8":
                stringify += "5"
            case "9":
                stringify += "6"
            case _:
                pass
    return stringify


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option = int(input('Please enter a option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
            print('')
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password} and the decoded password is {decoded_password}')
            print('')
        elif option == 3:
            break


if __name__ == '__main__':
    main()
