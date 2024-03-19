# program kalkulator sederhana
operator = str(input('pilih operator "penambahan", "pengurangan", "perkalian", atau "pembagian": '))

angka1 = int(input("Masukan angka pertama : "))
angka2 = int(input("Masukan angka kedua : "))

if operator == 'penambahan':
    res = angka1 + angka2
elif operator == 'pengurangan':
    res = angka1 - angka2
elif operator == 'perkalian':
    res = angka1 * angka2
elif operator == 'pembagian':
    res = angka1 / angka2

print(f'{operator} dari {angka1} dan {angka2} adalah {res}')
