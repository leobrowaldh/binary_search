import time
import random


def random_list(elements):
    """Creates a list of random non-duplicated elements. Consider that the list will probably contain fewer elements
    than the passed element parameter, because duplicates are ignored even though they count against this parameter."""
    the_list = []
    for i in range(elements):
        e = random.randrange(1, 10000, 1)
        if e not in the_list:
            the_list.append(e)
    return the_list


def normal_search(target, a_list):
    """Just a normal linear search through a list."""
    for i in range(len(a_list)):
        if a_list[i] == target:
            return i
    return -1


def binary_search(target, a_list):
    """Search for the target in a_list (must be sorted) using binary search, and return the index of the target.
    If target not found, it returns -1"""
    left = 0
    right = len(a_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if a_list[middle] == target:
            return middle
        elif a_list[middle] > target:
            right = middle - 1
        elif a_list[middle] < target:
            left = middle + 1

    return -1


if __name__ == '__main__':
    # First we create a random list and a random target in the list. (the list is unsorted)
    li = random_list(100000)  # Try passing 10, 100, 10000000, etc.
    ta = random.choice(li)
    # Now let's evaluate the performance of a normal linear search:
    start = time.time()
    normal_search(ta, li)
    end = time.time()
    normal_search_runtime = end - start
    print(f'normal search took {normal_search_runtime} seconds to complete.')
    # Now let's evaluate the performance of the binary search (including the time it takes to sort the list)
    start = time.time()
    li.sort()
    end = time.time()
    sorting_runtime = end - start
    print(f'sorting took {sorting_runtime} seconds')
    start = time.time()
    binary_search(ta, li)
    end = time.time()
    binary_search_runtime = end - start
    print(f'binary search took {binary_search_runtime} seconds to complete.')
    print(f'binary search, including sorting time took {sorting_runtime + binary_search_runtime} seconds to complete.')
    print('------------------------------------------------------------------')
    if (binary_search_runtime + sorting_runtime) < normal_search_runtime:
        print(f'binary search resulted {normal_search_runtime / (binary_search_runtime + sorting_runtime)} times '
              f'faster, sorting time included.')
    elif (binary_search_runtime + sorting_runtime) > normal_search_runtime:
        print(f'normal search resulted {(binary_search_runtime + sorting_runtime) / normal_search_runtime} times '
              f'faster, (sorting time included in the binary search).')
    print('If we don\'t include sorting time:')
    if binary_search_runtime < normal_search_runtime:
        print(f'binary search resulted {normal_search_runtime / binary_search_runtime} times faster.')
    elif binary_search_runtime > normal_search_runtime:
        print(f'normal search resulted {binary_search_runtime / normal_search_runtime} times faster.')

