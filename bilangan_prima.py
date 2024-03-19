def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % 1 == 0:
            return False
    return True
        
angka = float(input("masukan angka : "))

if is_prime(angka):
    print(f"{angka} adalah angka prima.")
else:
    print(f"{angka} bukan angka prima.")




# Deklarasi variabel
suhu_celsius =float(input("Input Suhu Celsius: "))

# Konversi suhu celsius ke fahrenheit
suhu_fahrenheit = (suhu_celsius * 9/5) + 32

# Konversi suhu celsius ke kelvin
suhu_kelvin = suhu_celsius + 273.15

# Konversi suhu celsius ke reamur
suhu_reamur = (suhu_celsius * 4/5)

# Cetak hasil konversi
print(f"{suhu_celsius} derajat Celsius = {suhu_fahrenheit} derajat Fahrenheit")
print(f"{suhu_celsius} derajat Celsius = {suhu_kelvin} derajat Kelvin")
print(f"{suhu_celsius} derajat Celsius = {suhu_reamur} derajat Reamur")



# Input suhu dalam Celsius
suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))

# Mengonversi suhu ke Fahrenheit
suhu_fahrenheit = (suhu_celsius * 9/5) + 32

# Menampilkan hasil konversi
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}")

