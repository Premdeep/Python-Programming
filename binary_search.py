# Binary search using recursion and defining function inside a function.

def search(L,e):
    def bsearch(L,e,low,high):
        if low == high:
            return e==L[low]
        mid = low + int((high-low)/2)
        if L[mid]==e:
            return True
        if L[mid] > e:
            return bsearch(L,e,low,mid-1)
        if L[mid] < e : # instead we could write else:
            return bsearch(L,e,mid+1,high)
                    
    if len(L) == 0:
        return False
    else:
        return bsearch(L,e,0,len(L)-1)

