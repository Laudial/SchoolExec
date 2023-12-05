def dichotomie(a, b, f, d):
    if f(a) * f(b) > 0:
        raise ValueError("La fonction n'a pas de zéro sur l'intervalle [a, b].")
    while b - a > d:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


print(dichotomie(2, 8, lambda x: x**2 - 10, 0.001))
