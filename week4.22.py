fp=open("word.txt","w")
if fp:
    print("successfully opened")
    fp.write("a ")
    fp.write("i")
    fp.write(" ")
    fp.close()