buku=["MateMatika","IPA"]

def show_data():
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print (indeks, buku[indeks])

show_data()
