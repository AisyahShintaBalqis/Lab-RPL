buku=["MateMatika","IPA"]

def show_data():
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print (indeks, buku[indeks])

show_data()

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    

insert_data()
show_data()


