buah=[]

def tampil():
    if len(buah) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buah)):
            print (indeks, buah[indeks])

tampil()
print("Tambahkan Data")
def tambahkan():
    buah_baru = input("Nama Buah: ")
    buah.append(buah_baru)
tambahkan()

tampil()
print("Edit Data")
def edit():    
    indeks = int (input("Inputkan ID buah: "))
    if(indeks > len(buah)):
        print ("ID salah")
    else:
        buah_baru = input("Nama Buah: ")
        buah[indeks] = buah_baru
edit()     


tampil()
print("Hapus Data")
def hapus():    
    indeks = int(input("Inputkan ID buah: "))
    if(indeks > len(buah)):
        print ("ID salah")
    else:
        buah.remove(buah[indeks])

hapus()
tampil()
