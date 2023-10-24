# Akshay Nandakumar

def encoder_function(number):
    number_list = [str(int(number[i]) + 3)[-1] for i in range(len(number))]
    return ''.join(number_list)



def main():
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
