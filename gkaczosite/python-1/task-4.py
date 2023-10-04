import random


def randomNumberGenerator(amountOfNumbers, minInteger, maxInteger):
    numberList = []

    i = 0
    while i < amountOfNumbers:
        number = random.randint(minInteger, maxInteger)

        numberList.append(number)

        i += 1

    return numberList


def listShuffler(listToShuffle):
    random.shuffle(listToShuffle)


def randomUniqueNumberGenerator(amountOfNumbers, minInteger, maxInteger):
    numberList = []

    if amountOfNumbers > maxInteger - minInteger:
        return 'There is not enough unique numbers'

    i = 0
    while i < amountOfNumbers:
        number = random.randint(minInteger, maxInteger)

        if numberList.count(number) != 0:
            continue

        numberList.append(number)

        i += 1

    return numberList


print(randomUniqueNumberGenerator(80, 1, 10))