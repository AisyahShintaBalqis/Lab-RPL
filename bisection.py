def inputdata(a,b):
    a= float(input("Masukan data awal a : "))
    b= float(input("Masukan data awal b : "))
    return (a,b)

def f(x):
    return (x**3- x - 6)

def checkAB(a,b):
    if(f(a)*f(b)== 0):
        return True
    else:
        return False

def updateData(a,b):
    c= (a+b)/2
    if(f(a)*f(c)== 0):
        b = c
    else :
        a = c
    return (a,b)

def process(a,b):
    while(abs(f(a)) or abs(f(b))):
        a,b = updateData(a,b)

    if(abs(f(a))>abs(f(b))):
        return b
    else:
        return a
    # return (a,b)
   

def main():
    a= 0
    b= 0    
    result = 0
    a,b = inputdata(a,b)
    if(checkAB(a,b)):
        print ("Data sesuai bisa dilanjutkan")       
        result = process(a,b)
        print ("Hasil = ",result," Dengan nilai f(x) ",f(result))
    else:
        print ("Data tidak sesuai tidak bisa dilanjutkan")
main()
