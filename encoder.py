# Akshay Nandakumar

def encoder_function(number):
    number_list = [str(int(number[i]) + 3)[-1] for i in range(len(number))]
    return ''.join(number_list)
