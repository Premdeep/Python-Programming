# program to print all substrings in a given string 

def substring(s):
    if len(s)== 0:
        return [""] 
    smaller = substring(s[:-1]) # string with out last element
    last = s[-1] # Last element
        
    print ("smaller is :",smaller)   
    print ("last element is :",last)
    r = []
    for small in smaller:
        print ("elements in smaller :",small)
        r.append(small+last)
        
    print ("r is :",r )
    print ("returned value is r+smaller :",r+smaller)
    print ("")
    return r+smaller

a =  substring("prem")
print ("All substrings in a given string [prem] are :")
print ("")
print (a)
