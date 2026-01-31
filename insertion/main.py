# insertion.py

def insertion_sort(input_array) -> list:
    """Sorts an array via insertion algorithm."""

    key = 1
    print(input_array)

    for i in range(0, len(input_array)-1):
        print("present: ", input_array[i])
        print("previous: ", input_array[i-1])
        print("next: ", input_array[i+1])
        print("\n")
        if input_array[i] < key:
            prev = input_array[-1]
            pres = input_array[i]
            input_array[i] = prev
            input_array[i+1] = pres

    return input_array

print(insertion_sort([5, 2, 8, 1, 9]))