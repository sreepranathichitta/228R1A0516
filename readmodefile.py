fp1=open("csea.txt","r")
if fp1:
    print("file is opened")
    fp1.seek(5, 0)
    for i in fp1:
        print(i)

'''content=fp1.readline()
print(content)
content=fp1.readline()
print(content)'''
fp1.close()

