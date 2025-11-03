def counting_sort(arr):
    # Handle empty or single-element arrays
    if not arr or len(arr) <= 1:
        return arr

    # Find the maximum element to determine the range of values
    max_val = max(arr)

    # Create a count array initialized with zeros
    # The size of count_arr is max_val + 1 to accommodate values from 0 to max_val
    count_arr = [0] * (max_val + 1)

    # Populate the count array: count occurrences of each element
    for num in arr:
        count_arr[num] += 1
    print(count_arr)
    # Modify the count array to store the actual position of each element
    # This step makes the sort stable (maintains relative order of equal elements)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    print(count_arr)

    # Create an output array to store the sorted elements
    output_arr = [0] * len(arr)

    # Build the output array from right to left to ensure stability
    j = len(arr)
    for num in reversed(arr):
        output_arr[count_arr[num] - 1] = num
        count_arr[num] -= 1  # Decrement count for subsequent equal elements
        print("At j=",j, "\n C[",num,"]=",count_arr[num]+1, "\nB=",output_arr, ", C=",count_arr, end="\n\n")
        j-=1

    return output_arr

# Example Usage:
my_list = [6,0,2,0,1,3,4,6,1,3,2]
sorted_list = counting_sort(my_list)
# print(f"Original list: {my_list}")
# print(f"Sorted list: {sorted_list}")

# my_list_2 = [10, 4, 1, 4, 7, 10]
# sorted_list_2 = counting_sort(my_list_2)
# print(f"Original list: {my_list_2}")
# print(f"Sorted list: {sorted_list_2}")