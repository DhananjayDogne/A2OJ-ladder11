#decrease each element by m in given list again and again while all not become zero and update ans each time

n,m=map(int,input().split())
l=list(map(int,input().split()))

ans=0
f=True

#Run untile all elements become zero
while f:
    f=False 
    for i in range(n):
        if l[i]>0:
            l[i]-=m 
            ans=i

        #there is one element ready for next round so,f=True
        if l[i]>0:
            f=True
 
        
print(ans+1)
