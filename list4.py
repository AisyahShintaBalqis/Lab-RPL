print ("===========================Mamuju Airport====================")

destinasi = []
maskapai = ['garuda','batik','lion']
kota = {"jakarta","makassar","palu","bali","jogja"}


def program():
    tujuan = input("Tambahkan tujuan anda : ")
    tujuan=tujuan.lower()
    if tujuan == "jakarta":
        destinasi.append(tujuan)
        if tujuan in destinasi :
            maska = input("Masukkan nama maskapai : ")
            maska=maska.lower()
            if maska == 'garuda':
                harga = 4000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            elif maska == 'batik':
                harga = 3000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            else:
                harga = 1500000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)

    elif tujuan == "makassar":
        destinasi.append(tujuan)
        if tujuan in destinasi :
            maska = input("Masukkan nama maskapai : ")
            maska=maska.lower()
            if maska == 'garuda':
                harga = 2000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            elif maska == 'batik':
                harga = 1500000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            else:
                harga = 1000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)

    elif tujuan == "palu":
        destinasi.append(tujuan)
        if tujuan in destinasi :
            maska = input("Masukkan nama maskapai : ")
            maska=maska.lower()
            if maska == 'garuda':
                harga = 3000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            elif maska == 'batik':
                harga = 2000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            else:
                harga = 1000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)

    elif tujuan == "bali":
        destinasi.append(tujuan)
        if tujuan in destinasi :
            maska = input("Masukkan nama maskapai : ")
            maska=maska.lower()
            if maska == 'garuda':
                harga = 4500000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            elif maska == 'batik':
                harga = 3500000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            else:
                harga = 3000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)

    elif tujuan == "jogja":
        destinasi.append(tujuan)
        if tujuan in destinasi :
            maska = input("Masukkan nama maskapai : ")
            maska=maska.lower()
            if maska == 'garuda':
                harga = 4000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            elif maska == 'batik':
                harga = 3000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)
            else:
                harga = 2000000
                print ("Silahkan melakukan pembayaran dengan harga : ",harga)


    else :
        print ("Maaf tujuan anda tidak dapat di tambahkan")

    

a = "y"
while(a == "y"):
    program()
    lanjut = input("Lakukan pembelian tiket lagi  (y/t) ?  ")
    lanjut=lanjut.lower()
    if lanjut !="y":
        break

print("Daftar tujuan anda ", destinasi)

    
