# episode operator bitwise, operasi biner, binary

from cgi import print_arguments
from re import X


a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n=========OR=========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('----------------------------- (|)')
print('nilai :', c, ' , binary :', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n=========AND========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('----------------------------- (&)')
print('nilai :', c, ' , binary :', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n=========XOR========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('nilai :', b, ' , binary :', format(b, '08b'))
print('----------------------------- (^)')
print('nilai :', c, ' , binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('\n=========NOT========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('----------------------------- (~)')
print('nilai :', c, ' , binary :', format(c, '08b'))
print('----------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e ^ d, ' , binary :', format(e ^ d, '08b'))

# shifting

# shift right (>>)
c = a >> 2
print('\n=========>>=========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('----------------------------- (>>)')
print('nilai :', c, ' , binary :', format(c, '08b'))

# shift left (<<)
c = a << 2
print('\n=========<<=========')
print('nilai :', a, ' , binary :', format(a, '08b'))
print('----------------------------- (<<)')
print('nilai :', c, ' , binary :', format(c, '08b'))
print("\n")

#Contoh program lain
x = 10
y = 12
print("====================================")
print("x adalah angka", x, "decimal atau", bin(x), "binner")
print("y adalah angka", y, "decimal atau", bin(y),"binner")

print("\n")
print("x | y  =", x | y)
print("x & y  =", x & y)
print("x ^ y  =", x ^ y)
print("~x     =", ~X)
print("x >> y =", x >> y)
print("x << y =", x << y)


