# run loop from x+1 to until next prime number is not found then match it with our real ans
# check funtion is used to check number is prime or not

def check(y):
    for x in range(2, (y//2) + 1):
        if y%x==0:
            return False 
    return True

x,y=map(int,input().split())
i=x+1
while True:
    if check(i):
        break
    i+=1

if i==y:
    print("YES")
else:
    print("NO")

