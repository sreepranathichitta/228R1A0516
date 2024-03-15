'''
1.open()
2.read()
3.readline()
4.write()
5.writeline()
6.seek()
7.tell()
8.close()
'''
fp=open("csea.txt","w")
if fp:
    print("file is created")
fp.write("good morning fellows\nhope you all had a great evening")    
fp.writelines("Im Pranathi\nRollno 516")
fp.close()