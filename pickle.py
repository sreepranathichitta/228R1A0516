import pickle
fp=open("picklefile.txt","wb")
s = ["hi","hello","good"]
pickle.dump(s,fp)
fp.close()