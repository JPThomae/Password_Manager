import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    nr_letters= 16
    nr_symbols = 3
    nr_numbers = 3


    total_char = nr_numbers +nr_letters +nr_numbers
    mega_list = []
    mega_password = ""
    ultra_mega_password = ""

    for x in range(1, nr_letters +1):
        pick_one = random.randint(0, len(letters) -1)
        mega_password += letters[pick_one]

    for x in range(1, nr_symbols +1):
        pick_one = random.randint(0, len(symbols) -1)
        mega_password += symbols[pick_one]

    for x in range(1, nr_numbers +1):
        pick_one = random.randint(0, len(numbers) -1)
        mega_password += numbers[pick_one]

    for x in mega_password:
        mega_list += x

    for x in range(0, len(mega_list) -1):
        pick_one = random.randint(0, len(mega_list) -1)
        ultra_mega_password += mega_list[pick_one]
        mega_list.remove(mega_list[pick_one])

    return ultra_mega_password

