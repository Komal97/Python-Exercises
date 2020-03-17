def segregate_array(arr, arr_size):
    j = 0
    for i in range(arr_size):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1
    print("arr", arr)
    return j

def find_missing_positive(arr, arr_size):
    print("positive arr: ", arr)
    for i in range(arr_size):
        if (abs(arr[i] - 1) < arr_size and arr[abs(arr[i] - 1)] > 0):
            arr[abs(arr[i] - 1)] = -arr[abs(arr[i] - 1)]
    print("negative arr: ", arr)

    for i in range(arr_size):
        if arr[i] > 0:
            return i+1
    return arr_size + 1

def find_missing_element(arr, arr_size):
    shift = segregate_array(arr, arr_size)
    return find_missing_positive(arr[shift:], arr_size - shift)

arr = [ 0, 10, 2, -10, -20 ] 
arr_size = len(arr)
missing_element = find_missing_element(arr, arr_size)
print("missing element :", missing_element)