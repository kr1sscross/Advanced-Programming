def zad3(numbers: list) -> list:
    result = []
    for i in range(5):
        result.append(numbers[i]*2)
    return result

numbers = [1, 2, 3, 4, 5]
print(zad3(numbers))