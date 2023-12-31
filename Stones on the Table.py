#count continues character if there ans add count-1 to answer

n=int(input())
s=input()
ans=0
i=0
while i<(n-1):
    count=0
    while i<n-1 and s[i]==s[i+1]:
          count+=1
          i+=1
    i+=1
    ans+=count

print(ans)
