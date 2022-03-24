# belajar class abstract

# membuat class abstract
# abc = abstract base class
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    def click(self):
        print("push button click")


tombol1 = PushButton()

tombol1.click()


"""
1. class biasa:
    -   instance-> object-> blueprint dari object
        * dia akan mengambil dari super class, tetapi kita bisa memilih mau di class atau di super class
2. class abstract
    - instance-> object-> blueprint dari class:
        * akan memaksa class untuk menginplementasikan methodnya.
        * tidak bisa langsung dibikin object
        * harus di buat dulu classnya sehingga bisa menginplementasikan classnya 
"""
