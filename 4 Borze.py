# map all the given code with substring 

s=input()
map={'.':0,'-.':1,'--':2}
sl=""
ans=""
for i in range(len(s)):
    sl+=s[i]
    if sl in map.keys():
        ans+=str(map[sl])
        sl=""
print(ans)
