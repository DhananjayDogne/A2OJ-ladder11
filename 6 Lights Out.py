#

mat=[[0,0,0,0,0]]
for i in range(3):
    mat.append([0]+list(map(int,input().split()))+[0])
mat.append([0,0,0,0,0])
eq=[]
for i in range(1,4):
    eq_row=[]
    for j in range(1,4):
        eq_row+=[mat[i][j]+mat[i+1][j]+mat[i-1][j]+mat[i][j+1]+mat[i][j-1]]
    eq.append(eq_row)
for i in range(3):
    for j in range(3):
        print((eq[i][j]+1)%2,end='')
    print('')
