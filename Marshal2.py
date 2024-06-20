import marshal
s='''
a=4
f=1
for i in range(1,a):
  f=f*1
print(f) '''
c=compile(s,"s,","exec")
fp=open("Marshal2.txt","wb")
marshal.dump(c,fp)
fp.close()