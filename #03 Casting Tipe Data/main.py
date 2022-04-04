import string
from xmlrpc.client import boolean


print("============BELAJAR CASTING TIPE DATA=============")
#casting adalah merubah dari satu tipe data ke tipe data lain
#TIPE DATA : INT, FLOAT, STR, BOOLEAN


#integer
print("==================================================")
data_int     = 34
data_float   = float(data_int)
data_str     = str(data_int)
data_boolean = bool(data_int)

print("data = ", data_int,"type   = ", type(data_int))
print("data = ", data_float,"type = ", type(data_int))
print("data = ", data_str,"type   = ", type(data_int))
print("data = ", data_int,"type   = ", type(data_int))


#float
print("==================================================")
data_float = 9.3
data_int   = int(data_float)
data_str   = int(data_float)
data_bool  = int(data_float)

print("data = ", data_float, "type   = ", type(data_float))
print("data = ", data_int, "type     = ", type(data_float))
print("data = ", data_str, "type     = ", type(data_float))
print("data = ", data_bool,"type     = ", type(data_float))