import shelve
#s=shelve.open("Shelve")or
with shelve.open("shelve") as s:
    s['one']=1
s.close()


