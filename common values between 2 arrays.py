a1=[1,2,3,4,5]
a2=[2,4,5,6,7,8,9]
common_array=[]
for i in a1:
    if i in a2:
        common_array.append(i)
print(common_array)