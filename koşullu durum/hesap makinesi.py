# basit hesap makinesi tasarlayınız.
print("""********************
HESAP MAKİNASI PROGRAMI 

İşlemler:

1.Toplama işlemi

2.Çıkarma işlemi

3.Çarpma işlemi

4.Bölme işlemi

********************
    """)

a=int(input("ilk sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
işlem=int(input("işlemi giriniz:"))

if(işlem == 1):
    print("{} ile {} 'in toplamı {}".format(a,b,a+b))
elif(işlem == 2):
    print("{} ile {} 'in farkı {}".format(a, b, a-b))
elif (işlem == 3):
    print("{} ile {} 'in çarpımı {}".format(a, b, a*b))
elif (işlem == 4):
    print("{} ile {} 'in bölümü {}".format(a, b, a/b))
else:
    print("GEÇERSİZ İŞLEM....")

