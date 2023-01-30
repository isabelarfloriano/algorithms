def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort(first_list)
    merge_sort(second_list)

    if (first_string == '' or second_list == ''):
        anagram = False
    else:
        anagram = first_list == second_list

    return (
        "".join(first_list),
        "".join(second_list),
        anagram,
    )


# Seção 4.3 - Trybe - Algoritmos que usam dividir e conquistar
def merge_sort(strings, start=0, end=None):
    if end is None:
        end = len(strings)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(strings, start, mid)
        merge_sort(strings, mid, end)
        merge(strings, start, mid, end)


def merge(strings, start, mid, end):
    left = strings[start:mid]
    right = strings[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            strings[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            strings[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            strings[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            strings[general_index] = right[right_index]
            right_index = right_index + 1
