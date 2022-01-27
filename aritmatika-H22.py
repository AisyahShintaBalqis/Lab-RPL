hargasemen = 50000

jumlah = int (input ("Jumlah Semen yang di beli : "))

if jumlah >= 100 :
    diskon = hargasemen * (2.5 / 100)
    harga = (hargasemen * jumlah) - diskon
    print ("Silahkan melakukan pembayaran sesuai dengan harga Rp.  ",harga)
elif jumlah >= 200 :
    diskon = hargasemen * (10 / 100)
    harga = (hargasemen * jumlah) - diskon
    print ("Silahkan melakukan pembayaran sesuai dengan harga Rp.  ",harga)

else :
    harga = hargasemen * jumlah
    print ("Silahkan melakukan pembayaran sesuai dengan harga Rp.  ",harga)
    
    
              
              
