tersedia = {'kambing','sapi','domba','kerbau','ayam'}
dicari = input ("hewan apa yang anda cari? ")
dicari=dicari.lower()
kambing = 2000000
sapi = 8000000
domba = 5000000
kerbau = 10000000
ayam = 80000

if (dicari in tersedia):
    print (dicari, "masih tersedia")
    if dicari == 'kambing' :
        berapa = int(input ("Berapa ekor yang anda mau ? "))
        if berapa <=100 :
            harga = int (kambing * berapa)
            print ("Silahkan Melakukan Pembayaran senilai Rp.",harga)
        else :
            print ("Maaf, Hewan yang tersedia tidak mencukupi")
            
    elif dicari == 'sapi' :
        berapa = int(input ("Berapa ekor yang anda mau ? "))
        if berapa <=50 :
            harga = int(sapi * berapa)
            print ("Silahkan Melakukan Pembayaran senilai Rp.",harga)
        else :
            print ("Maaf, Hewan yang tersedia tidak mencukupi")
    elif dicari == 'domba' :
        berapa = int(input ("Berapa ekor yang anda mau ? "))
        if berapa <=50 :
            harga = int(domba * berapa)
            print ("Silahkan Melakukan Pembayaran senilai Rp.",harga)
        else :
            print ("Maaf, Hewan yang tersedia tidak mencukupi")
    elif dicari == 'kerbau' :
        berapa = int(input ("Berapa ekor yang anda mau ? "))
        if berapa <=20 :
            harga = int(kerbau * berapa)
            print ("Silahkan Melakukan Pembayaran senilai Rp.",harga)
        else :
            print ("Maaf, Hewan yang tersedia tidak mencukupi")

    elif dicari == 'ayam' :
        berapa = int(input ("Berapa ekor yang anda mau ? "))
        if berapa <=150 :
            harga = int(ayam * berapa)
            print ("Silahkan Melakukan Pembayaran senilai Rp.",harga)
        else :
            print ("Maaf, Hewan yang tersedia tidak mencukupi")
            
    else :
        print ("Maaf tidak tersedia")
    

else :
    print ("Maaf, hewan yang anda cari tidak tersedia")

