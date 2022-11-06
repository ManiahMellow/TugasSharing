
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: ")) 

operator = input("Operator yang dipilih: ")

if(operator=="tambah" or operator=="penambahan"):
    tambah = angka1+angka2
    print(tambah)
elif(operator=="kurang" or operator=="pengurangan"):
    kurang = angka2-angka1
    print(kurang)
elif(operator=="perkalian" or operator=="kali"):
    kali = angka1*angka2
    print(kali)
elif(operator=="pembagian" or operator=="bagi"):
    if angka2 == 0:
        print("Bilangan tidak bisa dibagi 0")
    else:
        bagi = angka1/angka2
        print(bagi)



# #Penambahan bilangan bulat
# x = 5
# y = 8
# z = x+y
# print("Hasil penambahan adalah: ", z)

# #Penambahan Float
# a = 3.5
# b = 3.5
# c = a+b
# print("Hasil dari penambahan float adalah: ", c)

# #Penambahan boolean
# d = True
# e= False
# f = d+e
# print("Hasil dari penambahan boolean adalah: ", f)

# #Pengurangan bilangan bulat 
# satu = 16
# dua = 13
# hasil = satu-dua
# print("Hasil pengurangan bilangan bulat adalah: ", hasil)

# #Pengurangan float
# coba = 3
# coba2 = 2.5
# hasil1 = coba-coba2
# print("Hasil pengurangan float adalah: ", hasil1)

# #Pengurangan boolean
# satu1 = False
# satu2 = False
# hasil2 = satu1-satu2
# print("Hasil pengurangan boolean adalah: ", hasil2)

# #Perkalian 
# a1 = 4
# a2 = 5
# hasil3 = a1*a2
# print("Hasil perkalian adalah: ", hasil3)

# #Pembagian 
# a5 = 6
# a2 = 3
# hasil4 = a5/a2
# print("Hasil pembagian adalah: ", hasil4)

# #Pangkat 
# a7 = 4
# a8 = 5
# hasil6 = a7**a8
# print("Hasil perpangkatan adalah: ", hasil6)

# #Modulo
# a3 = 4
# a2 = 3
# hasil5 = a3%a2
# print("Hasil modulus adalah: ", hasil5)



