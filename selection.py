# using bubble sort method create another way to sort unsorted list
# using selection sort method create another way to sort unsorted list
# create a nesting loop that prints two lists. colors and cars


def while_bubble_sort(list):
    for i in range(len(list)):
        #    using while loop and subtracting 1 from current array size
        j = 0
        while j < len(list)-1:
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            j += 1
    return list


def while_selection_sort(list):
    for i in range(len(list)):
        # set min to first element in list and using while loop to find min
        min = i
        j = i
        while j < len(list):
            if list[j] < list[min]:
                min = j
            j += 1
        # swap min with first element in list
        list[i], list[min] = list[min], list[i]
    return list

# create a nesting loop that prints two lists. colors and cars
def nested_loop():
    colors = ['red', 'blue', 'green']
    cars = ['bmw', 'audi', 'toyota']
    for color in colors:
        for car in cars:
            print(color, car)


def main():
    list = [1, 5, 3, 2, 4]
    print("sorted with selection sort", while_selection_sort(list))
    print("sorted with bubble sort", while_bubble_sort(list))
    nested_loop()


if __name__ == '__main__':
    main()
