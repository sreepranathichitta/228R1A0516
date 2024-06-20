def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0
print("AND gate")
print(AND(1,0))
print(AND(0,1))
print(AND(0,0))
print(AND(1,1))
def OR(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1
print("OR gate")
print(OR(1,1))
print(OR(1,0))
print(OR(0,0))
print(OR(0,1))
def XOR(a,b):
    if a!=b:
        return 1
    else:
        return 0
print("XOR gate")
print(XOR(1,1))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(0,0))