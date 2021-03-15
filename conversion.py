###

# test = 0
# for i in input_number:

#     if i == "b":
#         test += 1
# print(test)

# Everything that's after b, x, or 0

# Fractional nums

def start():
    return (
        '''
Please, enter:
* the base of the number you're going to convert (BASE FROM)
* the base where you'd like to convert the number (BASE TO)
* the number to convert (NUMBER)

# Please, enter the number without any literals (0o, 0x, 0b, etc.). :) (NO LITERALS)
## Please, make sure if the format of the number format is correct. (CHECK NUMBER FORMAT)
    ''')

def check(base_in, base_out, number):

    legal = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'a', 'b', 'c', 'd', 
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 
             's', 't', 'u', 'v', 'w', 'x', 'y', 
             'z']
    
    if base_in not in range(2,37):
        print('Check the format of the input base (from 2 to 36)...')
        return False
    elif base_out not in range(2, 37):
        print('Check the format of the output base (from 2 to 36)...')
        return False
    else: 
        if base_in:
            for i in number:
                if i in legal[0:base_in]:
                    i
                else:
                    print('Check the number format...')
                    return False
        return True

def convert():

    legal = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']

    def length(number):
        len = 0
        for i in number:
            len += 1
        return len

    def to_decimal(base_in, number):
        power = len(number) - 1
        decimal = 0
        count = 0
        while count <= power:
            for i in number:
                decimal += int(legal.index(i)) * base_in ** (power - count)
                count += 1
        return decimal

    def to_output(decimal, base_out):
        reverse_number = []
        while decimal > 0:
            reverse_number += [decimal % base_out]
            decimal //= base_out
        index = length(number= reverse_number) - 1
        flip_number = []
        i = 0
        while i <= index:
            flip_number.append(reverse_number[index - i])
            i += 1
        output_number = ''
        for i in flip_number:
            output_number += legal[i]
        return output_number

    cont = True
    while cont:
        base_in = int(
            input("Enter the base of the number you're going to convert (2, 8, 10, etc.): "))
        base_out = int(input(
            "Enter the base where you'd like to convert the number (2, 8, 10, etc.): "))
        number = input("Enter the number to convert: ").lower()
        if check(base_in, base_out, number) == True:
            print(f'Converting {number} of the base of {base_in} to the base of {base_out}...')
            if base_in == base_out:
                print("Nothing to convert...")
            elif base_in == 10:
                decimal = int(number)
                result = to_output(decimal, base_out)
                print(f'{decimal} of the base of {base_in} is the {result} in the base of {base_out}')
            else:
                if base_out == 10:
                    decimal = to_decimal(base_in, number)
                    print(f'{number} of the base of {base_in} is the {decimal} in the base of {base_out}')
                else:
                    decimal = to_decimal(base_in, number)
                    result = to_output(decimal, base_out)
                    print(f'{number} of the base of {base_in} is the {result} in the base of {base_out}')   
            abc = input('Do you wish to convert another number? Type "yes" or "no": ').lower()
            if abc == 'no':
                cont = False

if __name__ == '__main__':
    print(start())
    convert()
