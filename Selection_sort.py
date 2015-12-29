# Selection sort Algorithm on Lists
# First we are going to find the smallest element in the 
# list and swap it with the first element and do the same
# like find the next smallest element in the remainig list
# and swap it with the second element and so on..

def sel_sort(L):
    for i in range(len(L)-1):
        min_index = i
        min_value = L[i]
        j = i+1
        while j < len(L):
            if min_value > L[j]:
                min_index = j
                min_value = L[j]
            j+=1
        temp = L[i]
        L[i] = min_value
        L[min_index] = temp       
 

L = [5,4,3,0,7,2,9]

print (L)

sel_sort(L)

print (L)
