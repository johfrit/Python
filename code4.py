count=0
s=input()
leng=len(s)
for i in range(0,leng,3):
    if s[i]!='S':
        count+=1
    if s[i+1]!='O':
        count+=1
    if s[i+2]!='S':
        count+=1
print(count)
    
    
    

