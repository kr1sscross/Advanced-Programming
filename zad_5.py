def zad4(numbers: list) -> list:
    result = []
    for i in range(0, 10, 2):
        result.append(numbers[i])

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(zad4(numbers))
