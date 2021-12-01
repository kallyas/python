# create simple bubble sort algorithm

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# create inverse bubble sort algorithm
def inverse_bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(inverse_bubble_sort([1,2,3,4,5,6,7,8,9,10]))

print(bubble_sort([17,2,89,3,34,50,6,7,89,9,10]))