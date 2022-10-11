# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def prime(num):
    if num > 1:
        found = False
        for i in range(2, num // 2):
            if (num % i) == 0:
                found = True
        return not found
    else:
        return False


def select_primes(arr):
    result = []
    for el in arr:
        if prime(el):
            result.append(el)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(select_primes([3, 6, 11, 25, 19]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
