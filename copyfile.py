fp1=open("csea.txt","r")
fp2=open("ecea.txt","w+")
if fp1:
    print("successfull")
for i in fp1:
    fp2.write(i)
print("file is copied successfully" )
fp2.seek(0,0)
content=fp2.read()
print(content)
fp1.close()
fp2.close()


