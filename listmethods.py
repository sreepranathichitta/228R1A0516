
'''
LIST METHODS:
1.sort()
2.clear()
3.append()
4.count()
5.extend()
6.insert()
7.index()
8.remove()
9.pop()
10.reverse()
11.copy()
12.len()
13.min()
14.max()
15.del()
'''
mylist=[1,5,6,8,11,3,2,4]
mylist.sort()
print(mylist)
mylist.append(50)
print(mylist)
mylist.extend([33,45,66])
print(mylist)
print(mylist.count(6))
max=max(mylist)
print(max)
min=min(mylist)
print(min)
del mylist[3]
print(mylist)
copylist=mylist.copy()
print("copy list=",copylist)
copylist.reverse()
print("reversed list=",copylist)





