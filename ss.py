def findSmall(arr):
    smallest = arr[0]
    smallIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallIndex = i
    return smallIndex

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmall(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

