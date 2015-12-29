# Linear search with out recursion

def linear_search(L,e):
    for i in L:
        if i == e:
            return True
        return False
    
# Linear search with Recursion    
def rec_search(L,e):
    if len(L) == 0:
        return False    
    if e == L[0]:
        return True
    if len(L)==1:
        return False
    else:
        return rec_search(L[1:],e)
    

# Binary search using recursion

def binary(L,e):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return e == L[0]
    mid = len(L)/2
    if L[mid] == e:  # we can skip this step 
        return True
    if L[mid] > e:
        return binary(L[:mid],e)
    else:
        return binary(L[mid+1:],e) # by replacing mid+1 to mid we can skip above step


# Binary search using recursion with less steps

def binary(L,e):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return e == L[0]
    mid = len(L)/2    
    if L[mid] > e:
        return binary(L[:mid],e)
    else:
        return binary(L[mid:],e) 
    
    
