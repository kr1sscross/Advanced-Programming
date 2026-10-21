def zad6(list1: list, list2: list) -> list:
    mlist = list1 + list2
    mlist = list(set(mlist))
    flist = []

    for num in mlist:
        flist.append(num*num*num)

    return flist


if __name__ == "__main__":
    print(zad6([2, 4, 8], [2, 6, 8, 10]))
