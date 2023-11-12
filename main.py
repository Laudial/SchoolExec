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

        listB[i], listB[listMin] = listB[listMin], listB[i]

    return listB

print(noSort(listA))
