import math
import random
import statistics


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def addVectors(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result


def multipleVectors(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    return result


def scalar(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        result += (arr1[i] * arr2[i])
    return result


def euclides(arr1):
    result = 0
    for i in range(len(arr1)):
        result += (arr1[i] * arr1[i])
    return math.sqrt(result)


def randomArray():
    result = []
    for i in range(50):
        result.append(random.randint(1, 100))
    return result


def taskE(arr):
    minimum = min(arr)
    print(minimum)
    maximum = max(arr)
    print(maximum)
    mean = statistics.mean(arr)
    sum = 0
    for i in range(len(arr)):
        sum += math.pow(arr[i] - mean, 2)
    print(math.sqrt((sum / len(arr))))


def taskF(arr):
    minimum = min(arr)
    maximum = max(arr)
    result = []
    for i in range(len(arr)):
        result.append((arr[i] - minimum) / (maximum - minimum))
    print(result)


def standardisation(arr):
    mean = statistics.mean(arr)
    sum = 0
    for i in range(len(arr)):
        sum += math.pow(arr[i] - mean, 2)
    deviation = math.sqrt((sum / len(arr)))
    result = []
    for i in range(len(arr)):
        result.append((arr[i] - mean) / deviation)
    print(result)


def discretization(arr):
    result = []
    for el in arr:
        if el >= 0 and el < 10:
            result.append("[0, 10)")
        elif el >= 10 and el < 20:
            result.append("[10, 20)")
        elif el >= 20 and el < 30:
            result.append("[20, 30)")
        elif el >= 30 and el < 40:
            result.append("[30, 40)")
        elif el >= 40 and el < 50:
            result.append("[40, 50)")
        elif el >= 50 and el < 60:
            result.append("[50, 60)")
        elif el >= 60 and el < 70:
            result.append("[60, 70)")
        elif el >= 70 and el < 80:
            result.append("[70, 80)")
        elif el >= 80 and el < 90:
            result.append("[80, 90)")
        elif el >= 90 and el <= 100:
            result.append("[90, 100]")

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr1 = [3, 8, 9, 10, 12]
    arr2 = [8, 7, 7, 5, 6]
    print(addVectors(arr1, arr2))
    print(multipleVectors(arr1, arr2))
    print(scalar(arr1, arr2))
    print(euclides(arr2))
    print(euclides(arr1))
    randomArr = randomArray()
    print(randomArr)
    taskE(randomArr)
    taskF(randomArr)
    standardisation(randomArr)
    print(discretization(randomArr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
