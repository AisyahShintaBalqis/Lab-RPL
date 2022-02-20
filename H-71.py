def katakan(pesan, jumlah=1):
    print (pesan * jumlah)

katakan('Halo ')
katakan('Halo ', 3)


def fungsi(a, b=5, c=10):
    print ('a = ', a)
    print ('b = ', b)
    print ('c = ', c)

fungsi(3, 7)
fungsi(25, c=24)
fungsi(c=50, a=100)
