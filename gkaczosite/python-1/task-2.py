# Write a program that, for the elements (1, 5, 7, 2, 9, 2, 7, 2) placed in a tuple,
# will perform the following actions:

print('tuple assignment')

tupleForAssignment = (1, 5, 7, 2, 9, 2, 7, 2)

# Display the content of the tuple

for number in tupleForAssignment:
    print(number)

print('')
# provide information on how many times '2' occurs

occurrencesOf2 = 0

for number in tupleForAssignment:
    if number == 2:
        occurrencesOf2 += 1

print(occurrencesOf2)

print('')
# Display information about the number of elements

amountOfNumbers = 0

for number in tupleForAssignment:
    amountOfNumbers += 1

print(amountOfNumbers)

print('')
# Display the largest number

largestNumber = 0

for number in tupleForAssignment:
    if number > largestNumber:
        largestNumber = number

print(largestNumber)

print('')
# Display the three last elements

for x in range(-3, 0):
    print(tupleForAssignment[x])
