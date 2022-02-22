x = 20

def fungsi():
    print ("x = ", x)

def fungsi2():
    x = 100  # menulis ke lokal variabel
    print ("x = ", x)

def fungsi3():
    global x
    
    print ("x = ", x)

fungsi()

fungsi2()


fungsi3()
