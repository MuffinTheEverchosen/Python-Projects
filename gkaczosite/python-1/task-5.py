import re


def stringToUpperCase(text):
    return text.upper()


def firstLetterToUpperCase(text):
    textInList = list(text)

    i = 0
    for letter in textInList:
        if not re.search("\W", letter):
            textInList[i] = letter.upper()
            break

        i += 1

    return ''.join(textInList)


def searchForLook(text):
    found = re.search('(look)', text)

    if not found:
        return 'No "look" in text'

    position = found.span()[0]

    return position


def checkIfAnythingOtherThanDigitsOrLetterExist(text):
    check = re.search("\W", text)
    if check:
        return 'True'
    else:
        return 'False'


def deleteWhitespaces(text):
    textWithoutWhitespaces = text.replace(' ', '')

    return textWithoutWhitespaces


def seperateWords(text):
    seperateWords = re.split("\s", text)

    return seperateWords


def eraseFirstAndLastIndex(text):
    textList = list(text)

    textList.pop()
    textList.pop(0)

    return ''.join(textList)


def iDontEvenKnowAnymore(text):
    text = text.replace("Always look on the bright side of life", "Always look on the bright side of your life")

    return text


text = "Always look on the bright side of life"
