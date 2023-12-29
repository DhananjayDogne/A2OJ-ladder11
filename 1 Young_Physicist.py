#Calculate sumation of all the given coordinates and check for equilibrium condition

def f():
    n=int(input())
    x=y=z=0
    for i in range(n):
        a,b,c=map(int,input().split())
        x+=a
        y+=b
        z+=c
    #Check Equlibrium condition
    if x==0 and y==0 and z==0:
        print("YES")
    else:
        print("NO")
    
if __name__ == '__main__':
    f()
