import random
import matplotlib.pyplot as plt
import numpy as np


def theor(condition):
    list_pr = []
    if condition == 0:
        list_pr.append(1)
    elif condition == 1:
        list_pr.append(0)

    matrix = np.array([[0.8, 0.2], [0.6, 0.4]])
    p0 = np.array([1, 0])

    for step in range(1, 30):
        p0 = p0.dot(matrix)
        list_pr.append(p0[condition])
    return list_pr


def prob(n, t, condition):
    flag = condition
    count = 0
    p00 = 0.8
    p11 = 0.4

    if not condition and t == 0:
        return 0
    for j in range(0, n):
        for step in range(0, t):
            c = random.random()
            if flag:
                if c > p00:
                    flag = False
            else:
                if c > p11:
                    flag = True
        if condition == flag:
            count += 1
    return count / n


listPrcondition0 = []
listT = []

for t in range(0, 30):
    listT.append(t)
    listPrcondition0.append(prob(50000, t, True))


list_pr0 = theor(0)

plt.figure()
plt.plot(listT, listPrcondition0, color='red', label='Condition(0)')
plt.plot(listT, list_pr0, color='blue', label='Theor(0)')
plt.legend()
plt.xlabel('T(time)')
plt.ylabel('Pr(prob)')
plt.savefig('R30.png')
plt.show()