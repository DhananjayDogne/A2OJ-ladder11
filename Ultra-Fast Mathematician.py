# take xor or compare at each index

s=input()
s2=input()
ans=""
for i in range(0,len(s)):
    if s[i]==s2[i]:
        ans+=str(0) 
    else:
        ans+=str(1)


print(ans)
