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

# fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int (input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
edit_data()
    
    
show_data()


