def read_mat(a,r,c):
    for i in range(r):
        t=[]
        for j in range(c):
            v=int(input(f"Enter the a[{i}][{j}] value"))
            t.append(v)
        a.append(t)
def display_mat(a):
    for i in a:
        print(i)
mat_a=[]
read_mat(mat_a,2,2)
print("matrix a")
display_mat(mat_a)
mat_b=[]
read_mat(mat_b,2,2)
print("matrix b")
display_mat(mat_b)
c=[]
for i in range(2):
    t=[]
    for j in range(2):
        val = mat_a[i][j] + mat_b[i][j]
        t.append(val)
    c.append(t)
display_mat(c)





