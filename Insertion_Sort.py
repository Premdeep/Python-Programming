# program implementing the insertion sort. Insertion sort is better than
# Bubble sort and selection sort. which are pretty close.

# To know how insertion sort works check this out

# http://www.studytonight.com/data-structures/insertion-sorting

L = [5,1,6,2,4,3]

def insertsort(L):
    for j in range(1,len(L)):
        for i in range(j):
            if L[i]> L[j]:
                L[i],L[j] = L[j],L[i]
    return L


# other program:

def pair(L):
    a = []
    high = max(L) 
    for i in range(len(L)-1):        
        x = abs(L[i]-L[i+1])        
        if x<=high:
            high = x            
            a.append(L[i])
            a.append(L[i+1])        
    return a

        

   
