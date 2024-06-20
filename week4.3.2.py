#s="pranathi kusumita manogna"
#w="pranathi"
def remove(s,w):
    x=s.replace(w,' ')
    return x
s1="pranathi kusumita manogna"
s2=remove(s1,"pranathi")
print(s2)