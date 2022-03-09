# problem 1 -------------------------------------------------------
from audioop import reverse


def max_num(num1, num2):
    if num1 > num2:
        return num1
    return num2


print("problem 1 sol ", max_num(8, 6))


# problem 2 ------------------------------------------------------
def factorial(number):
    temp = 1
    while number >= 1:
        temp *= number
        number -= 1
    return temp


print("problem 2 sol ", factorial(4))


# problem 3 ------------------------------------------------------
def list_reverse(list):
    return list.reverse()


def list_reverse2(list):
    return list[::-1]


def list_reverse3(inpList):
    return list(reversed(inpList))


x = [5, 6, 8, 1]
list_reverse(x)
print("problem 3 sol ", x)

x = [5, 6, 8, 1]
x = list_reverse2(x)
print("problem 3 sol ", x)

x = [5, 6, 8, 1]
x = list_reverse3(x)
print("problem 3 sol ", x)


# problem 4 -----------------------------------------------------
def print_list(list):
    list.sort()
    print("problem 4 sol ", list)
    list.sort(reverse=True)
    print("problem 4 sol ", list)


list = [4, 9, 7, 3, 8]
print_list(list)


# problem 5 ------------------------------------------------------
def max_tuple(list):
    temp = []
    maximum = ''
    for tup in list:
        maximum = tup[0]
        for num in range(1, len(tup)):
            if maximum < tup[num]:
                maximum = tup[num]
        temp.append(maximum)
    return temp


x = [(2, 5, 3), (8, 7, 1), (3, 7, 9)]
print("problem 5 sol ", max_tuple(x))


# problem 6 ------------------------------------------------------
def insert_at(list, item, index):
    list.insert(index, item)


list = [4, 3, 7]
insert_at(list, 5, 1)
print("problem 6 sol ", list)


# problem 7 -----------------------------------------------------
def list_len(list):
    return len(list)


list = [5, 8, 9, 7]
print("problem 7 sol ", list_len(list))


# problem 8 -----------------------------------------------------
def find_item(list, item):
    if item in list:
        return True
    return False


list = [7, 8, 1, 6]
print("problem 8 sol ", find_item(list, 6))


# problem 9 --------------------------------------------------------
def calc_y(start_range, end_range):
    temp = []
    index = start_range
    while index <= end_range:
        y = (index**2) + (4 * index) + 3
        temp.append(y)
        index += 1
    return temp


print("problem 9 sol ", calc_y(-4, 4))


# problem 10 --------------------------------------------------------
def list_average(list):
    return sum(list) / len(list)


list = [3, 5, 7, 2]
print("problem 10 sol ", list_average(list))


# problem 11 -------------------------------------------------------
def item_remove(list, index):
    list.pop(index)


list = [1, 3, 8, 6]
print("problem 11 sol ", list)
item_remove(list, 1)
print("problem 11 sol ", list)


# problem 12 -----------------------------------------------------
def convert_to_dec(number):
    if not number.startswith(('-o', 'o')):
        return print("Invalid Value")

    power = 0
    res = 0
    temp = number
    number = number.replace('o', '')
    number = number.replace('-', '')

    try:
        int(number)
    except:
        return print("Invalid Value")

    if number == '8' or number == '9':
        return print("invalid digit " + number + " in octal literal")

    number = number[::-1]
    for i in number:
        res = res + (int(i) * (8**power))
        power += 1

    if '-' in temp:
        return print("Decimal Value = ", f'{"-"}{res}')

    return print("Decimal Value = ", res)


def convert_to_oct(num):
    temp = str(num)
    res = ''

    if '-' in temp:
        num = temp.replace('-', '')

    try:
        num = int(num)
    except:
        return print("Invalid Value")

    while num > 0:
        res = str(num % 8) + res
        num = int(num / 8)

    if '-' in temp:
        return print("Octal Value = ", f'{"-"}{res}')

    return print("Octal Value = " + res)


def dec_oct(num):
    number = str(num)
    number = number.replace('O', 'o')
    if 'o' in number:
        return convert_to_dec(number)

    return convert_to_oct(num)


dec_oct(input("Enter Value = "))


# another solution for problem 12 ---------------------------------------------------
def convert_to_dec(number):
    if not number.startswith(('-o', 'o')):
        return print("Invalid Value")

    number = number.replace("o", '')

    try:
        return print("Decimal Value = ", int(number, 8))
    except:
        return print("Invalid Value")


def convert_to_oct(number):
    try:
        number = int(number)
    except:
        return print("Invalid Value")

    return print("Octal Value = ", oct(number).replace("0o", ""))


def dec_oct(num):
    number = str(num)
    number = number.replace('O', 'o')
    if 'o' in number:
        return convert_to_dec(number)

    return convert_to_oct(num)


dec_oct(input("Enter Value = "))


# problem 13 ------------------------------------------------------
def convert_hex_to_dec(number):
    if not number.startswith(('-h', 'h')):
        return print("Invalid Value")

    number = number.replace('h', '')

    try:
        res = int(number, 16)
    except:
        return print("Invalid Value")

    return print("Decimal Value = ", res)


def convert_to_hex(num):
    try:
        number = int(num)
    except:
        return print("Invalid Value")

    hex_val = hex(number)

    hex_val = hex_val.replace('0x', '')

    return print("Hex Value = ", hex_val)


def hex_dec(num):
    number = str(num)
    number = number.replace('H', 'h')
    if 'h' in number:
        return convert_hex_to_dec(number)

    return convert_to_hex(num)


hex_dec(input("Enter Value = "))


# problem 14 -------------------------------------------------------
def factorial_rec(num):
    if(num >= 1):
        return num * factorial_rec(num - 1)
    return 1


print("problem 14 sol ", factorial_rec(6))
