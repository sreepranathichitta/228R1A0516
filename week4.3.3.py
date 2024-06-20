#s="welcome to prerana towers"
'''ord()------>convert char to ascii
chr()---->convert acsii to char'''
def convert(s):
    c=list(s)
    for i in range(len(s)):
        if i==0 and c[i]!=' ':
            if c[i]>='a'and c[i]<='z':
                c[i]=chr(ord(c[i])-ord('a')+ord('A'))
    s="",c[i]
    return s
print(convert("welcome hi"))
