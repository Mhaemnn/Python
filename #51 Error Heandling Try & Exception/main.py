ukuran_sepatu = input('Berapakah ukuran sepatu anda?\n')

try:
    ukuran_sepatu = int(ukuran_sepatu)
    print('Terima kasih atas infonya, ukuran sepatu anda ', ukuran_sepatu)
    print('Kami akan carikan ukuran yang sesuai')
except:
    print('Nilai ukuran sepatu yang anda masukkan tidak valid')
"""
    type of exception error:
     1. IOError
     2. ImportError
     3. ValueError
     4. Devision by Error
     5. KeyboardInterupted
     6. EOFError 
     
"""