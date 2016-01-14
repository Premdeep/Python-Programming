# Finding GCD using recursion

def GcdRec(a, b):
    if a == b:
        return a
    else:
        if a == 0 or b == 0:
            return max(a,b)
        else:
            if a>b:
                return 1*Gcd(a%b,b)
            else:
                return 1*Gcd(a,b%a)
        

# Finding Gcd by Iteration 

def GcdItr(a,b):
    x = min(a,b)
    while(x>=1):
        if(a%x == 0):
            if(b%x == 0):
                return x
        x = x-1

# Finding Gcd with another recursion method

def GcdRec1(a,b):
    x = min(a,b)
    y = max(a,b)
    if x == 1:
        return x
    elif a%x == 0 and b%x == 0:
        return x
    else:
        return GcdRec1(x,y%x)


# Finding GCD with another recursion method

def GcdRec2(a,b):
    if a == b or b == 0:
        return a
    else:
        return GcdRec2(b,a%b)
