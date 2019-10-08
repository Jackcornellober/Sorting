# TO-DO: complete the helper function below to merge 2 sorted arrays

import math

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    for i in range(elements):
      if len(arrA) and len(arrB):
        if arrA[0] > arrB[0]:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[i] = arrA[0]
            arrA.pop(0)
      elif len(arrA): 
        merged_arr[i] = arrA[0]
        arrA.pop(0)
      elif len(arrB): 
        merged_arr[i] = arrB[0]
        arrB.pop(0)
        
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        arr1 = []
        arr2 = []
        for i in range(0,math.floor(len(arr)/2)):
            arr1.append(arr[i])
            
        for i in range(math.floor(len(arr)/2),len(arr)):
            arr2.append(arr[i])
            
        print(arr1)
        print(arr2)
        arr = merge(merge_sort(arr1),merge_sort(arr2))
        print(arr)


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
