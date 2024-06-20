import marshal
fp=open("Marshal2.txt","rb")
d=marshal.load(fp)
exec(d)