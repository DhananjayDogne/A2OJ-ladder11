#swap if B is before G and move on t times same

n,t=map(int,input().split())
s=input()
ans=[i for i in s]
count=0 
 
while t>=1:
    i=1
    while i<n:
        if ans[i-1]=='B' and ans[i]=='G':
            ans[i-1]='G'
            ans[i]='B'
            i+=1
        i+=1
    t-=1
res=""
for i in ans:
    res+=i
print(res)
