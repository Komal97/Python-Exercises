a = [2, 23, 14, 7, 32, 29]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("The unsorted list is : ", a)
print("The sorted list is : ", bubble_sort(a))


