def zad2(numbers: list) -> list:
    result = []
    for number in numbers:
        result.append(number*2)

    return result

numbers = [1, 2, 3, 4, 5]
print(zad2(numbers))