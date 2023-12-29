l=[]
x,y=0,0
for i in range(5):
    l.append(list(map(int,input().split())))
       
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            x=i 
            y=j 
 
print(abs(2-x)+abs(2-y))
