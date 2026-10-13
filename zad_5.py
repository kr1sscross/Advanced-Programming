def zad5(nums: list, num: int) -> bool:
    if num in nums:
        return True
    else:
        return False

if __name__ == "__main__":
    print(zad5([1, 2, 3, 4, 5],3))