### Плюсы сортировки quick sort:
## В среднем работает быстрыее других сортировок
# Алгоритм разделяет массив на подмассивы относительно опорного элемента, что позволяет эффективно обрабатывать данные.
# В связи с этим меньше пар для сравнений
# Хорошие результаты по производительности при работе с большими массивами


def arr_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return arr_sort(left) + middle + arr_sort(right)

