# merge sort procedure is all about understanding how recursion works

def merge(left,right):
    res = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            res.append(right[j])
            j+=1
        else:
            res.append(left[i])
            i+=1
    while i < len(left):
        res.append(left[i])
        i+=1
    while j< len(right):
        res.append(right[j])
        j+=1
    return res

# THis piece of code above describes how the sorting works since the problem
# is broken down in to smaller sub problem the merge function works best because
# first it compares two lists with only one element in each and sorts them
# This goes on such that every time it gets a new list it will be in sorted form

def mergeSort(L):
    if len(L) < 2:
        return L
    mid = len(L)//2  # interger division
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left,right)  # this does the sorting of all the lists

# Time complexity is O(len(L)) * O(log(len(L))) so total is O(nlogn)
