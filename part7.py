# operasi logika atau boolean
# not , or, and xor
# NOT


print("========= NOT =========")
a = True
b = not a
print("nilai dari b = ", b)
 
# OR
print("========= OR(atau) =========")
print("hasil akan true, selama ada satu saja true")
a = False
b = False
hasil = a or b
print(a, "OR", b, "=", hasil)
a = False
b = True
hasil = a or b
print(a, "OR", b, "=", hasil)
a = True
b = False
hasil = a or b
print(a, "OR", b, "=", hasil)
a = True
b = True
hasil = a or b
print(a, "OR", b, "=", hasil)

# AND
print("========= AND =========")
print("hasil akan true, jika keduanya true")
a = False
b = False
hasil = a and b
print(a, "AND", b, "=", hasil)
a = False
b = True
hasil = a and b
print(a, "AND", b, "=", hasil)
a = True
b = False
hasil = a and b
print(a, "AND", b, "=", hasil)
a = True
b = True
hasil = a and b
print(a, "AND", b, "=", hasil)

# XOR
print("========= XOR =========")
print("hasil akan true, jika salah satu true, tetapi tidak keduanya")
a = False
b = False
hasil = a ^ b  # XOR operator adalah ^
print(a, "XOR", b, "=", hasil)
a = False
b = True
hasil = a ^ b
print(a, "XOR", b, "=", hasil)
a = True
b = False
hasil = a ^ b
print(a, "XOR", b, "=", hasil)
a = True
b = True
hasil = a ^ b
print(a, "XOR", b, "=", hasil)