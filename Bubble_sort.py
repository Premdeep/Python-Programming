# Bubble sort Algorithm

def BubbleSort(s):
    if len(s)<=1:
        return s
    check = False
    while not check:
        check = True  # Important because bubble sort checks only two elements at a time
        for i in range(len(s)-1):
            j = i+1
            if s[i]>s[j]:
                check = False # This will make the sort to take place again
                s[j],s[i] = s[i],s[j]
    return s
                
            
