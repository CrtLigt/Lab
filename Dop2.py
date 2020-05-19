
import random
import matplotlib.pyplot as plt
import numpy as np


def theoretical(matrix):
    vector = np.array([0, 0, 1])
    matrix_transpose = np.transpose(matrix)
    matrix_transpose[2] = np.array([1, 1, 1])
    matrix_transpose[0, 0] -= 1
    matrix_transpose[1, 1] -= 1
    temp_vector = np.linalg.solve(matrix_transpose, vector)
    return temp_vector


def practical(matrix, time):
    current_state = 0
    count_state0 = 0
    count_state1 = 0
    count_state2 = 0

    for i in range(0, time):
        c = random.random()
        if current_state == 0:
            if c < matrix[0][0]:
                current_state = 0
            elif c < (matrix[0][0] + matrix[0][1]):
                current_state = 1
            else:
                current_state = 2
        elif current_state == 1:
            if c < matrix[1][0]:
                current_state = 0
            elif c < (matrix[1][0] + matrix[1][1]):
                current_state = 1
            else:
                current_state = 2
        else:
            if c < matrix[2][0]:
                current_state = 0
            elif c < (matrix[2][0] + matrix[2][1]):
                current_state = 1
            else:
                current_state = 2
        if current_state == 0:
            count_state0 += 1
        elif current_state == 1:
            count_state1 += 1
        elif current_state == 2:
            count_state2 += 1
    print("Практика (0): ", count_state0 / time)
    print("Практика (1): ", count_state1 / time)
    print("Практика (2): ", count_state2 / time)


def print_practical(matrix, time, state):
    current_state = 0
    count = 0
    n = 5000

    for i in range(0, n):
        for j in range(0, time):
            c = random.random()
            if current_state == 0:
                if c < matrix[0][0]:
                    current_state = 0
                elif c < (matrix[0][0] + matrix[0][1]):
                    current_state = 1
                else:
                    current_state = 2
            elif current_state == 1:
                if c < matrix[1][0]:
                    current_state = 0
                elif c < (matrix[1][0] + matrix[1][1]):
                    current_state = 1
                else:
                    current_state = 2
            else:
                if c < matrix[2][0]:
                    current_state = 0
                elif c < (matrix[2][0] + matrix[2][1]):
                    current_state = 1
                else:
                    current_state = 2
        if state == current_state:
            count += 1
    return count / n


def print_graphics(matrix):
    time_list = []
    list_pr_state0 = []
    list_pr_state1 = []
    list_pr_state2 = []

    for time in range(0, 100):
        time_list.append(time)
        list_pr_state0.append(print_practical(matrix, time, 0))
        list_pr_state1.append(print_practical(matrix, time, 1))
        list_pr_state2.append(print_practical(matrix, time, 2))

   # plt.figure()
   # plt.plot(time_list, list_pr_state0, color='red', label='State(0)')
   # plt.plot(time_list, list_pr_state1, color='green', label='State(1)')
   # plt.plot(time_list, list_pr_state2, color='blue', label='State(2)')
   # plt.legend()
   # plt.xlabel('T(time)')
   # plt.ylabel('Pr(probability)')
   # plt.savefig('script2.png')
   # plt.show()


def main():
    matrix = [[0.8, 0.2, 0], [0.3, 0.35, 0.35], [0, 0.7, 0.3]]
    time = 250000

    print("Теоретические значения: ", theoretical(matrix))
    practical(matrix, time)
    print_graphics(matrix)


main()
