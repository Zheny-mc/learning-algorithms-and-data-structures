from typing import List


# def quick_sort(array, get_elem):
#     if len(array) <= 1:
#         return array
#
#     elem = get_elem(array[0])
#     left = list(filter(lambda x: get_elem(x) > elem, array))
#     center = [i for i in array if get_elem(i) == elem]
#     right = list(filter(lambda x: get_elem(x) < elem, array))
#
#     return quick_sort(left, get_elem) + center + quick_sort(right, get_elem)

def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    heights_i = {}
    for i in range(len(names)):
        heights_i[i] = heights[i]
    sorted_height = {key: val for key, val in sorted(heights_i.items(), key=lambda item: item[1], reverse=True)}

    return [names[key] for key in sorted_height]


print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
print(sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))