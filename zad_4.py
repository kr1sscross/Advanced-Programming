def zad4(numbers: list) -> list:
    result = []
    for i in range(10):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
        else:
            continue


    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(zad4(numbers))