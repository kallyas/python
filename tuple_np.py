import numpy as np

# create a tuple with a list of items and convert it to a list
def create_tuple(length):
    t = ()
    for i in range(length):
        t += (i,)
    return list(t)

# Add two more items the list and then convert it back to a tuple
def add_two_items(t):
    t += [2, 3]
    return tuple(t)

# create a 3-D numpy array
def create_3d_array(n):
    # return a 3-D array with n for 3 rows and 3 columns
    return np.array([[[i, i, i] for i in range(n)]])

# create a function that print odd numbers using numpy
def print_odd_numbers(n):
    for i in range(n):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    print(create_tuple(5))

    tp = create_tuple(5)
    print(add_two_items(tp))

    print(create_3d_array(3))

    print_odd_numbers(15)
