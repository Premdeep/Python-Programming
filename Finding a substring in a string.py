# finding no.of times a substring appears in a string

s = "abcbobdefbobahfalflkagldabcaef"

s1 = "bob"

i = 0
r = 0

while len(s)-3 > i:
    if s[i:i+3] == s1:
        r += 1
    i+=1

        
        
print (r)
