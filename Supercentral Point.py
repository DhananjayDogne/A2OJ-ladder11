# check each point by 1 more loop according to conditions given in question

n=int(input() )
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append([x,y])
    
ans=0
for i in range(n):
    f1=False 
    f2=False
    f3=False
    f4=False
    for j in range(n):
        
        if l[i][0]<l[j][0] and l[i][1]==l[j][1]:
            f1=True
        if l[i][0]>l[j][0] and l[i][1]==l[j][1]:
            f2=True
        if l[i][0]==l[j][0] and l[i][1]<l[j][1]:
            f3=True
        if l[i][0]==l[j][0] and l[i][1]>l[j][1]:
            f4=True
    if f1 and f2 and f3 and f4:
        ans+=1 
print(ans)
