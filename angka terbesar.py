# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input("Masukkan Angka Pertama :"))
b = int(input("Masukkan Angka Kedua :"))
c = int(input("Masukkan Angka Ketiga :"))

maks = 0

print (a, b, c,)

if a > b:
    maks = a
else:
    maks = b

if c > maks:
    maks = c
    
print("Angka Terbesar Adalah : ",maks)
    