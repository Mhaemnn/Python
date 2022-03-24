# belajar Method Resolution Oder -> Lanjutan multiple inheritance


class A:
    def show_A(self):
        print("ini adalah show A")


class B:
    def show_B(self):
        print("ini adalah show B")


class C(A, B):
    pass


object = C()

# jadi method resolution order yang di inheritace ke sebuah class itu tergantung dari urutanya
# ini berlaku jika penamaanya sama
