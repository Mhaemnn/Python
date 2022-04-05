
print("============BELAJAR CASTING TIPE DATA=============")
#casting adalah merubah dari satu tipe data ke tipe data lain
#TIPE DATA : INT, FLOAT, STR, BOOLEAN


#integer
print("======================integer======================")
data_int     = 34
data_float   = float(data_int)
data_str     = str(data_int)
data_bool    = bool(data_int)

print("data = ", data_int,"type   = ", type(data_int))
print("data = ", data_float,"type = ", type(data_float))
print("data = ", data_str,"type   = ", type(data_str))
print("data = ", data_int,"type   = ", type(data_bool))


#float
print("======================float========================")
data_float = 9.5
data_int   = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)

print("data = ", data_float,"type  = ", type(data_float))
print("data = ", data_int,"type    = ", type(data_int))
print("data = ", data_str,"type  = ", type(data_str))
print("data = ", data_bool,"type = ", type(data_bool))


#boolean
print("======================boolean=======================")
data_bool = True
data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool)

print("data = ", data_bool, "type = ", type(data_bool))
print("data = ", data_int, "type    = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_float, "type  = ", type(data_float))

#string
print("======================string=========================")
data_str   = "29";
data_int   = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool  = bool(data_str) #false jika string kosong

print("data = ", data_str, "type   = ", type(data_str))
print("data = ", data_int, "type   = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))