class A:
    def method(self):
        print("class  A is defined")
        super().method()
class B:
    def method(self):
        print("class B is defined")
        super().method()
class c(A,B):
    def method(self):
        print("c class is defined")
        super().method()
obj=c()
obj.method()

