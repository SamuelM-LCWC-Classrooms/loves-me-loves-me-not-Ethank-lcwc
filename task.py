
def Loves_me(number):
    numbers1 = []
    numbers = []
    num1 = 0
    while num1 != number:
        num1 = num1 + 1
        numbers1.append(num1)
    for i in numbers1:
        if i == number:
            if i % 2 == 0:
                i = "LOVES ME NOT"
                numbers.append(i)
            else:
                i = "LOVES ME"
                numbers.append(i)
        else:
            if i % 2 == 0:
                i = "Loves me not"
                numbers.append(i)
            else:
                i = "Loves me"
                numbers.append(i)
    numbers = str(numbers)

    return numbers
print(Loves_me(6))


