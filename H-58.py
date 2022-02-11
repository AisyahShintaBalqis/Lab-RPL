def salam(ucapan):
    print(ucapan)

salam("Selamat siang")

def salam(ucapan, sapaan):
    print(ucapan, sapaan)
salam("Assalamualaikum","Haii")

def salam(ucapan, sapaan, tanya):
    print(ucapan, sapaan, tanya)

salam("Assalamualaikum","Haii","Apa Kabar?")

nama = "Aisyah"
nim = "D0219305"

def help():
    # ini variabel lokal
    nama = "Balqis"
    nim = "d0219305"
    # mengakses variabel lokal
    print ("Nama: ", nama)
    print ("nim: ", nim)


# mengakses variabel global
print ("Nama: ", nama)
print ("nim: ", nim)

# memanggil fungsi help()
help()

