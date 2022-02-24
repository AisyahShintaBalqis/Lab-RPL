destinasi = []
kota = "jakarta","makassar","palu","bali","jogja","mamuju","malang","bandung","malang","medan","padang","jayapura","ambon"



def program():
    tujuan = input("Tambahkan tujuan anda : ")
    tujuan=tujuan.lower()
    if tujuan in kota:
        destinasi.append(tujuan)

    elif tujuan in kota:
        destinasi.append(tujuan)

    elif tujuan in kota:
        destinasi.append(tujuan)

    elif tujuan in kota:
        destinasi.append(tujuan)

    elif tujuan in kota:
        destinasi.append(tujuan)

    else :
        print ("Maaf tujuan anda tidak dapat di tambahkan")

    

a = "y"
while(a == "y"):
    program()
    lanjut = input("Masih mau menambahkan y/t ?  ")
    lanjut=lanjut.lower()
    if lanjut !="y":
        break

print("Daftar tujuan anda ", destinasi)

    
