def zad3(num: int) -> bool:
    tf = bool(num % 2 == 0)

    return tf

if __name__ == "__main__":
    if zad3(5):
        print("Even")
    else:
        print("Odd")
