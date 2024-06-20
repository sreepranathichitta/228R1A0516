import shelve
s=shelve.open("shelve","r")
print(list(s.keys()))
