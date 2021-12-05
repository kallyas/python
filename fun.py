
def selection_sort_recursive(arr):
    count = 0
    temp = []
    
    # check if item at index count is the smallest, then swap 
    # with the first item in the array
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)):
            if arr[i] < arr[count]:
                count = i
        temp.append(arr[count])
        arr.pop(count)
        return temp + selection_sort_recursive(arr)

       


if __name__ == "__main__":
    arr = [1, 4, 2, 5, 3, -8, -2, -1, -3, -4, -5, -6, -7, -9, -10]
    print(selection_sort_recursive(arr))
   
