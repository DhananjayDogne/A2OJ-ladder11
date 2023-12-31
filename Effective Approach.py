#store all the element index wise in a map ,then cal comparision which is equal to index+1 number for Vashay and n-index for Sasha's

n=int(input())
l=list(map(int,input().split()))

n2=int(input())
q=list(map(int,input().split()))

ans1=0
ans2=0

#store in map accoring to index
map={}
for i in range(n):
    map[l[i]]=i

#compare for both vashay and Sasha's
for i in range(n2):
    ind=map[q[i]]
    ans1+=ind+1
    ans2+=n-ind

print(ans1,ans2)
