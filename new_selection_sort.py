# selection sort in the shortest number of steps but expensive complexity

def new_sel(L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]

