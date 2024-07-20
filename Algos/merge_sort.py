""" 
    =- Code Structure
    1. Make Two Function `merge_sort` and `merge`
"""

def merge(arr, start_idx, midIdx, endIdx):
    i, j, k

    left_list = []
    right_list = []

    i = j = 0
    k = start_idx

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[i]:
            arr[k] = left_list[i]
            i += 1
        else:
            arr[k] = right_list[j]
            j += 1
        k += 1

def merge_sort(arr, start_idx, end_idx):
    if start_idx > end_idx:
        return
    midIdx = (end_idx - start_idx) // 2
    merge_sort(arr, start_idx, midIdx)
    merge_sort(arr, midIdx + 1, end_idx)
    merge(arr, start_idx, midIdx, end_idx)