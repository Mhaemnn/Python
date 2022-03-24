# belajar multiple inheritance

class A:
    def method_A(self):
        print("ini adalah method A")


class B:
    def method_B(Self):
        print("ini adalah Method B")


class C(A, B):
    pass


object = C()

object.method_A()
object.method_B()


"""
1. multiple inheritance adalah suatu class yang bisa mendapatakan inheritance dari banyak class
2. 
"""
