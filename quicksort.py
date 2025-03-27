def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i  for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

lst = [5, 10, 20, 2, 3]
result = quicksort(lst)

print(result)
