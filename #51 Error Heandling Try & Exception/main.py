ukuran_sepatu = input('Berapakah ukuran sepatu anda?\n')

try:
    ukuran_sepatu = int(ukuran_sepatu)
    print('Terima kasih atas infonya, ukuran sepatu anda ', ukuran_sepatu)
    print('Kami akan carikan ukuran yang sesuai')
except:
    print('Nilai ukuran sepatu yang anda masukkan tidak valid')
