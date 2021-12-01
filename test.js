// create bubble sort function
function bubbleSort(arr) {
    // loop through array
    for (let i = 0; i < arr.length; i++) {
        // loop through array again
        for (let j = 0; j < arr.length; j++) {
        // if the current value is greater than the next value
        if (arr[j] > arr[j + 1]) {
            // swap the values
            let temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
        }
    }
    return arr;
    }

    // create an array of numbers
    let arr = [5, 3, 7, 2, 1, 9, 6, 8, 4];
    // call the bubble sort function
    bubbleSort(arr);
    // print the array
    console.log(arr);