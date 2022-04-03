print("===BELAJAR CASTING TIPE DATA====")
# belajar casting tipe data: merubah dati satu data kedata lain
# tipe data: int, float, string, boolean


# INTEGER 
print("===========INTEGER==========")
data_int = 9
print("data=", data_int, "type=", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # akan flase jika nilai int=0
print("data=", data_float, "type=", type(data_float))
print("data=", data_str, "type=", type(data_str))
print("data=", data_bool, "type=", type(data_bool))


# FLOAT
print("===========FLOAT==========")
data_float = 9.7
print("data=", data_float, "type=", type(data_float))

data_int = int(data_float)  # akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai float bernilai = 0
print("data=", data_int, "type=", type(data_int))
print("data=", data_str, "type=", type(data_str))
print("data=", data_bool, "type=", type(data_bool))


# STRING
print("===========STRING==========")
data_str = "23"
print("data=", data_str, "type=", type(data_str))

data_int = int(data_str)  # string harus angka
data_float = float(data_str)  # string harus anka
data_bool = bool(data_str)  # akan false jika string kosong
print("data=", data_int, "type=", type(data_int))
print("data=", data_float, "type=", type(data_float))
print("data=", data_bool, "type=", type(data_bool))


# BOOLEAN
print("===========BOOLEAN==========")
data_boolean = True
print("data=", data_boolean, "type=", type(data_boolean))

data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = float(data_boolean)  # akan flase jika nilai int=0
print("data=", data_int, "type=", type(data_int))
print("data=", data_str, "type=", type(data_str))
print("data=", data_float, "type=", type(data_float))
