import numpy as np
from random import random
import matplotlib.pyplot as plt


P = np.array([[0.8, 0.2], ## P00 P01
             [0.4, 0.6]]) ## P10 P11

t = 20
N = 100000
p_t = [0] * t

listT = []
listT = list(range(0, t))

def theor():
    state = 0
    list_pr = []
    if state == 0:
        list_pr.append(1)
    elif state == 1:
        list_pr.append(0)

    matrix = P
    p0 = np.array([1, 0])

    for step in range(1, t):
        p0 = p0.dot(matrix)
        list_pr.append(p0[state])
    return list_pr

for n in range(N):
    state = 0
    for i in range(t):
        p_t[i] += state ^ 1
        next_distr_p = random()
        if next_distr_p < P[state][0]:
            state = 0
        else:
            state = 1

p_t[:] = (i / N for i in p_t)

distr = np.array([1, 0]) ##p0(t) p1(t)
list_pr0 = theor()

fig = plt.figure()
plt.plot(listT, p_t, color="g", label="p_t")
plt.plot(listT, list_pr0, color="m", label="p_t_theor")
plt.legend()
plt.show()
