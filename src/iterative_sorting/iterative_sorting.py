# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for g in range(i,len(arr)):
            if arr[g] < arr[smallest_index]:
                smallest_index = g
        arr[smallest_index],arr[cur_index] = arr[cur_index],arr[smallest_index]
        
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    finished = 0
    while finished == 0:
        change_made = 0
        for index, q in enumerate(arr):
            if index+1 !=len(arr):
                if q > arr[index+1]:
                    arr[index],arr[index+1] = arr[index+1],arr[index]
                    change_made = 1
        if change_made == 0:
            finished = 1


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return 


print(bubble_sort([5,3,4,2,1]))

print(selection_sort([5,3,4,2,1]))

x = 1
y = 2

print(x)
print(y)

x,y = y,x

print(x)
print(y)

arr = ['lol','lol2']

arr[1],arr[0] = arr[0],arr[1]

print[arr]