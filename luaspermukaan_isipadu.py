# Atur cara mengira luas permukaan dan isipadu silinder
# Isytihar pemalar
pi = 3.142

# Input
jejari = float(input("Masukkan jejari:"))
tinggi = float(input("Masukkan tinggi:"))

# Proses
luaspermukaan = 2 * pi * (jejari**2) + 2 * pi * jejari * tinggi
isipadu = pi * (jejari**2) * tinggi

# Output
print("Luas permukaan ialah",round(luaspermukaan,2))
print("Isi padu ialah",round(isipadu,2))
