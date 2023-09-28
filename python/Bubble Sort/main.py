def swap(_List: list, index: int, swap_index: int):

    _List[index], _List[swap_index] = _List[swap_index], _List[index]

    return _List


def bubble_sort(List: list):
    for i in range(0, len(List) - 1):
        swapped = False
        for j in range(0, (len(List) - 1)):
            if List[j] > List[j + 1]:
                swap(List, j, j + 1)
                swapped = True
        if not swapped:
            break
    return List


def selection_sort(List: list):
    for i in range(len(List)):
        selected = None
        for j in range(0 + i, len(List)):
            if selected == None or List[j] < selected:
                selected = List[j]
                swap_index = j
        swap(List, swap_index, i)
    return List


print(" b - " ,bubble_sort([4, 6 ,3, 21, 8, 9, 3 ,45, 74, 65, 12]), " s - ", selection_sort([4, 6 ,3, 21, 8, 9, 3 ,45, 74, 65, 12]))
