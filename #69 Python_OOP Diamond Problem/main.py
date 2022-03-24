# belajar diamond problem -> lanjutan dari multiple inheritance

class A:
    def show(self):
        print("ini adalah show A")


class B(A):  # class B yang menginheritance class A
    def show(self):
        print("ini adalah show B")


class C(A):
    def show(self):
        print("ini adalah show C")


class D(B, C):
    pass
