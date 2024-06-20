#TRY AND EXCEPT
'''try:
    a=10
    b=0
    print(a/b)
except Exception:
    print("cannot divide by zero")
finally:
    print("finally block is executed")'''
#NAME EXCEPTION
'''try:
    a=10
    c=a/b
    print(c)
except Exception:
    print("b is not mentioned")
print("handling the exceptions")'''
#VALUE EXCEPTION
'''try:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)
except Exception:
    print("value exception")'''
#INDEX EXCEPTION
'''try:
    a=[1,2,3,4,5,6]
    print(a[7])
except Exception:
    print("index exception")'''
#KEY EXCEPTION
'''try:
    a={"pranathi":"1","kusumita":"2","manogna":"3"}
    print(key["anirudh"])
except Exception:
    print("key exception")'''
#INPUT OR OUTPUT ERROR
'''try:
    fp=open("pranu.txt")
except Exception:
    print("file exception")'''
#RAISE EXCEPTION
a=int(input())
b=int(input())
if b==0:
    raise print("Raise Exception Handling")
else:
    print(a/b)