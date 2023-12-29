#check each next term 


s=int(input())
s+=1
def h(x):
    x=str(x)
    l=[]
    for i in range(len(x)):
        if x[i] not in l:
            l.append(x[i]) 
        else:
            return True 
    return False
while h(s):
    s+=1
print(s)


