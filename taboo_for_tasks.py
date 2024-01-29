import random
import sys

import numpy as np
import pandas as pd

# Function calculates time from the given order of tasks
# array - matrix of times
# order - order from which we calculate time


def get_time(array, order):
    tmp = np.zeros(shape=(array.shape[0], array.shape[1]), dtype=int)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            tmp[i, j] = max(tmp[i - 1, j], tmp[i, j - 1]) + array[order[i], j]

    return tmp[array.shape[0] - 1, array.shape[1] - 1].copy()


# Function checks for normal_swap and array_swap variants whether a given swap is on the taboo list
# i, j - indices to check
# taboo - taboo list


def is_not_on_taboo(i, j, taboo):
    if taboo[i, j] != 0 and taboo[j, i] != 0:
        return False
    else:
        return True


# Function checks for the pos_swap variant whether a given swap is on the taboo list
# i, j - indices to check
# taboo - taboo list


def is_not_on_taboo2(i, j, taboo):
    if taboo[i, j] != 0:
        return False
    else:
        return True


# Function updates the taboo list for array_swap and normal_swap variants, decreases non-zero values by 1, and adds a specified value to the given cell
# taboo - taboo list
# punishment - penalty value for the swap
# i, j - coordinates for which to set the punishment value


def taboo_act(taboo, punish, k, m):
    for j in range(taboo.shape[0]):
        for i in range(taboo.shape[0]):
            if taboo[j, i] != 0:
                taboo[j, i] = taboo[j, i] - 1

    taboo[k, m] = punish
    taboo[m, k] = punish
    return taboo


# Function updates the taboo list for the pos_swap variant, decreases non-zero values by 1, and adds a specified value to the given cell
# taboo - taboo list
# punishment - penalty value for the swap
# i, j - coordinates for which to set the punishment value


def taboo_act2(taboo, punish, k, m):
    for j in range(taboo.shape[0]):
        for i in range(taboo.shape[0]):
            if taboo[j, i] != 0:
                taboo[j, i] = taboo[j, i] - 1

    taboo[k, m] = punish

    return taboo


# Function swaps two values in the list
# order - list in which to change the order
# i, j - coordinates of two positions in the list to be swapped


def normal_swap(order, i, j):
    tmpOrder = order.copy()
    tmpOrder[i], tmpOrder[j] = tmpOrder[j], tmpOrder[i]
    return tmpOrder


# Function swaps positions in the list by rotating the entire slice between the given coordinates
# order - list in which to change the order
# i, j - coordinates of two positions in the list to be swapped


def array_swap(order, i, j):
    tmpOrder = order.copy()
    for k in range((j - i + 1) // 2):
        tmpOrder[i + k], tmpOrder[j - k] = tmpOrder[j - k], tmpOrder[i + k]

    return tmpOrder


# Function swaps tasks in the list by inserting the task from index i to index j
# order - list in which to change the order
# i - coordinates of the task index to be swapped
# j - coordinates of the index where the task will be inserted


def pos_swap(order, i, j):
    tmpOrder = order.copy()
    tmpOrder = tmpOrder.tolist()
    variable = tmpOrder.pop(i)
    tmpOrder.insert(j, variable)
    tmpOrder = np.array(tmpOrder)
    return tmpOrder


# Function searches the neighborhood of the given order and finds the best non-taboo swap for array_swap or normal_swap
# array - matrix of distances between tasks
# order - list to search for the best neighborhood
# taboo - taboo list
# Note: Choose between array_swap and normal_swap by commenting out the appropriate type of swap in the function get_best_swap


def get_best_swap(array, order, taboo):
    bestLoopOrder = order.copy()
    bestLoopDistance = sys.maxsize

    for i in range(0, order.size - 1):
        for j in range(i + 1, order.size):
            if is_not_on_taboo(order[i], order[j], taboo):
                # tmpOrder = normal_swap(order, i, j)
                tmpOrder = array_swap(order, i, j)

                if get_time(array, tmpOrder) < bestLoopDistance:
                    bestLoopDistance = get_time(array, tmpOrder)
                    bestLoopOrder = tmpOrder
                    X = order[i]
                    Y = order[j]

    return bestLoopDistance, bestLoopOrder, X, Y


# Function searches the neighborhood of the given order and finds the best non-taboo swap for pos_swap
# array - matrix of distances between tasks
# order - list to search for the best neighborhood
# taboo - taboo list


def get_best_swap2(array, order, taboo):
    bestLoopOrder = order.copy()
    bestLoopDistance = sys.maxsize

    for i in range(0, order.size):
        for j in range(0, order.size):
            if is_not_on_taboo2(order[i], j, taboo) and i != j:

                tmpOrder = pos_swap(order, i, j)
                if get_time(array, tmpOrder) < bestLoopDistance:
                    bestLoopDistance = get_time(array, tmpOrder)
                    bestLoopOrder = tmpOrder
                    X = order[i]
                    Y = j

    return bestLoopDistance, bestLoopOrder, X, Y


# Main function that provides individual best times for the variant where a certain number of iterations is given
# punishment - penalty for the swap
# reps - number of iterations
# bestOrder - initial order of tasks
# bestDistance - time calculated from the initial order
# Note: Depending on the type of swap to be checked, add 2 (for pos_swap) or not (for array_swap or normal_swap) in the get_best_swap function


def MainFoo(punishment, reps, bestOrder, bestDistance):

    print("First  Order:", bestOrder)
    print("First Distance:", bestDistance)
    topTmpDistance = bestDistance
    topTmpOrder = bestOrder
    for n in range(1, reps):
        print(n / reps)
        topTmpDistance, topTmpOrder, X, Y = get_best_swap2(ar, topTmpOrder, taboo)

        if topTmpDistance < bestDistance:
            bestDistance = topTmpDistance.copy()
            bestOrder = topTmpOrder.copy()

        taboo_act(taboo, punishment, X, Y)

    print("Best Order:", bestOrder)
    print("Best Distance:", bestDistance)


# Main function that provides individual best distances for the variant where a certain number of iterations without improvement is given
# punishment - penalty for the swap
# reps - number of iterations without improvement
# bestOrder - initial order of tasks
# bestDistance - distance calculated from the initial distance
# Note: Depending on the type of swap to be checked, add 2 (for pos_swap) or not (for array_swap or normal_swap) in the get_best_swap function


def MainFoo2(punishment, reps, bestOrder, bestDistance):
    # data=[]
    print("First  Order:", bestOrder)
    print("First Distance:", bestDistance)
    topTmpDistance = bestDistance
    topTmpOrder = bestOrder
    i = 0
    n = 1
    while i < reps:
        print(n)
        topTmpDistance, topTmpOrder, X, Y = get_best_swap(ar, topTmpOrder, taboo)
        print(topTmpDistance)

        print(bestDistance)

        if topTmpDistance < bestDistance:
            bestDistance = topTmpDistance.copy()
            bestOrder = topTmpOrder.copy()
            i = 0
        taboo_act(taboo, punishment, X, Y)

        print(i / reps)
        i = i + 1
        n = n + 1
    print("Best Order:", bestOrder)
    print("Best Distance:", bestDistance)
    print("Number of reps:", n)


# Set print options for NumPy
np.set_printoptions(threshold=sys.maxsize)

# Read data from an Excel file
# Note: Data should
df = pd.read_excel("Dane_PFSP_100_10.xlsx")

# Convert DataFrame to NumPy array
ar = df.to_numpy()

# Remove the first column from the array
ar = np.delete(ar, 0, 1)

# Generate a random initial order of cities
bestOrder = list(range(ar.shape[0]))
random.shuffle(bestOrder)
bestOrder = np.array(bestOrder)
bestTmpOrder = bestOrder
bestDistance = get_time(ar, bestOrder)

# Initialize the taboo list
taboo = np.zeros((ar.shape[0], ar.shape[0]), dtype=int)


# Run main function
MainFoo(25, 100, bestOrder, bestDistance)
