import random


def G(n):
    return n & (n + 1)


def A(ls: list, index):
    result = 0
    for ind in range(G(index), index+1):
        result += ls[ind]
    return result


a = [random.randint(0, 100) for i in range(10)]
t = [A(a, i) for i in range(10)]
print(a)
print(t)


def sumo(x):
    res = 0
    while x >= 0:
        res += t[x]
        x = G(x)-1
    return res


def sum(L: int, R: int) -> int:
    if L:
        return sumo(R) - sumo(L-1)
    else:
        return sumo(R)


def addToElement(i, aa, lll = t):
    while i < len(a):
        lll[i] += aa
        i |= (i+1)
    return lll


def prefixSum(K):
    result = 0
    i = K
    while i > 0:
        result += t[i]
        i = G(i)-1
    return result


def modifyElement(i, aa):
    current = prefixSum(i) - prefixSum(i-1)
    return addToElement(i, aa-current)

aaa, b = int(input("Введите а: ")), int(input("Введите b: "))
print("Сумма Фенвика: " + str(sum(aaa, b)))
index1 = int(input("Введите индекс: "))
count = int(input("Введите сколько нужно добавить: "))
print("Добавление: " + str(addToElement(index1, count)))
index2 = int(input("Введите индекс: "))
mod = int(input("Введите на что надо поменять: "))
print("Модификация: " + str(modifyElement(index2, mod)))
