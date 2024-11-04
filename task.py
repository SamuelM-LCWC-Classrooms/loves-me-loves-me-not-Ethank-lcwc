
def loves_me(number):
    numbers1 = []
    numbers = str()
    num1 = 0
    while num1 != number:
        num1 = num1 + 1
        numbers1.append(num1)
    for i in numbers1:
        if i == number:
            if i % 2 == 0:
                i = "LOVES ME NOT"
                numbers = numbers + " " + i
            else:
                i = "LOVES ME"
                numbers = numbers + " " + i
        else:
            if i % 2 == 0:
                i = "Loves me not,"
                numbers = numbers + " " + i
            else:
                i = "Loves me,"
                numbers = numbers + " " + i
    

    return numbers


