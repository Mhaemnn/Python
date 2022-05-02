"""
method adalah code yang berisi sebuah fungsi yang dapat digunakan
dalam suatu class 
"""

class product(): #class
    nama_product = 'nama product' # attribute
    
    def dataProduct(self,kondisi): # method dataProduct dan kondisi
        print(self.nama_product, ": buku tulis dengan harga", kondisi) # memanggil nama attribute

beli = product() # instansiasi
beli.dataProduct(340000) # memanggil nama method dan masukan kondisi
