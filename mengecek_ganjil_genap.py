# program untuk mengecek ganjil-genap dari suatu angka
a = int(input("masukan angka awal: "))
b = int(input("masukan angka akhir: "))

for i in range(a, b+1):
    if i%2 == 0:
        res = 'genap'
    elif i%2 != 0:
        res = 'ganjil'
    print(i, res)

"""
Jika menggunakan print di baris baru, maka
hanya satu angka yang akan di eksekusi.
"""