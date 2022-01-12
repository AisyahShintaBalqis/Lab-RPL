print ("==================Warnet WWW===================")

kode_p = input ("Kode Pelanggan : ")
kode_p = kode_p.lower()
durasi = int(input ("Waktu Sewa : "))

if kode_p == 'p' :
    tarif = 4000
    if durasi >= 5 :
        harga = tarif * durasi
        diskon = harga * (50 / 100)
        total = harga - diskon
        print ("Selamat, anda mendapatkan diskon 50% berdasarkan durasi sewa anda, Silahkan lakukan pembayaran dengan nominal Rp. ",total)

    elif durasi >= 3:
        harga = tarif * durasi
        diskon = harga * (30 / 100)
        total = harga - diskon
        print ("Selamat, anda mendapatkan diskon 30% berdasarkan durasi sewa anda, Silahkan lakukan pembayaran dengan nominal Rp. ",total)
    else :
        print ("Silahkan lakukan pembayaran dengan nominal Rp. ",total)
else :
    tarif = 5000
    if durasi >= 5 :
        harga = tarif * durasi
        diskon = harga * (50 / 100)
        total = harga - diskon
        print ("Selamat, anda mendapatkan diskon 50% berdasarkan durasi sewa anda, Silahkan lakukan pembayaran dengan nominal Rp. ",total)

    elif durasi >= 3 :
        harga = tarif * durasi
        diskon = harga * (30 / 100)
        total = harga - diskon         
        print ("Selamat, anda mendapatkan diskon 30% berdasarkan durasi sewa anda, Silahkan lakukan pembayaran dengan nominal Rp. ",total)
    else :
        print ("Silahkan lakukan pembayaran dengan nominal Rp. ",total)
