def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no elements were swapped, the list is already sorted
        swapped = False

        # Last i elements are already in place, so we ignore them
        for j in range(0, n - i - 1):

            # Compare the element adjacent to it
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return arr


# Test the function
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(test_list)
print(f"Sorted array: {sorted_list}")
