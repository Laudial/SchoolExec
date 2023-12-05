import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def dichotomie(a, b, f, e):
    m = (a + b) / 2
    while abs(b - a) > e:
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
        m = (a + b) / 2
    return f"{m:.2f}"


if __name__ == "__main__":

    clear()

    nbA = random.randint(1, 100)
    nbB = random.randint(1, 100)
    
    print(dichotomie(nbA, nbB, lambda x: x**2 - 10, 0.001))
