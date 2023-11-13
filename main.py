import os
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

listA = [random.randint(-10, 10) for i in range(10)]

def noSort(listB):
    for i in range(len(listB)):
        listMin = i

        for j in range(i + 1, len(listB)):
            if listB[j] < listB[listMin]:
                listMin = j

        listB[listMin], listB[i] = listB[i], listB[listMin]

    return listB

clear()

print(noSort(listA))
