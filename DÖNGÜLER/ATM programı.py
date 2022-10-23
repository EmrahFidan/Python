# ATM makinesi örneği

print("""
**************
ATM makinesine hoşgeldiniz

işlemler:
1. Bakiye sorgulama
2. para yatırma
3. para çekme

programdan çıkmak için 'q' ya basın.
**************
""")

bakiye = 3000

while True:
    işlem = input("işleminizi seçin:")
    if(işlem == "q"):
        print("Yine bekleriz")
        break
    elif(işlem == "1"):
        print("bakiyeniz : {} tl'dir.".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("yatırmak istediğiniz para miktarını giriniz:"))
        bakiye += miktar
        print("bakiyeniz : {} tl'dir.".format(bakiye))
    elif (işlem == "3"):
        miktar = int(input("çekmek istediğinizz para miktarını giriniz:"))
        if(bakiye - miktar < 0):
            print("yeterli bakiyeye sahip değilsiniz")
            continue
        bakiye -= miktar
        print("bakiyeniz : {} tl'dir.".format(bakiye))
    else:
        print("geçersiz işlem")
