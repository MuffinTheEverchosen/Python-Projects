def removeTwoFirstChars(localStr):
    localList = list(localStr)
    localList.pop(0)
    localList.pop(0)
    return ''.join(localList)


# Write a program that, for elements of a given integer:
integer = input('Please input integer: ')
integer = int(integer)
mode = 2

match mode:
    case 0:
        # will convert it to binary
        binary = bin(integer)

        binary = removeTwoFirstChars(binary)

        print(binary)

        # will convert it to octal
        octal = oct(integer)

        octal = removeTwoFirstChars(octal)

        print(octal)

        # will convert it to hexadecimal
        hexadecimal = hex(integer)

        hexadecimal = removeTwoFirstChars(hexadecimal)

        print(hexadecimal)

    case 1:
        # will convert a number from binary form to an integer
        binary = str(integer)
        decimal = int(binary, 2)

        print(decimal)

    case 2:
        # for a given integer, will remove the last two bits from the binary representation of the number
        binary = bin(integer)

        binary = removeTwoFirstChars(binary)

        binaryInList = list(binary)

        if binaryInList:
            binaryInList.pop()
        if binaryInList:
            binaryInList.pop()

        if binaryInList:
            binary = ''.join(binaryInList)

            print(binary)
            print(int(binary, 2))
        else:
            print('nothing is here')

