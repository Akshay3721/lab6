# Akshay Nandakumar

def encoder(number):
    number_list = [str(int(number[i]) + 3)[-1] for i in range(len(number))]
    return ''.join(number_list)
def decoder(number):
    return


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
            encoded_password = encoder_function(password)
            print('Your password has been encoded and stored!')
            print('')
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password} and the decoded password is {decoded_password}')
            print('')
        elif option == 3:
            break