s=input()
low=0
for i in s:
    if i.islower():
        low+=1
if low>=len(s)/2:
    print(s.lower())
else:
    print(s.upper())


