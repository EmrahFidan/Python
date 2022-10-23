# Faktoriyel bulma

print("""
****************************

faktoriyel bulma programı

çıkmak için "q" ya basın

****************************
""")

while True:
    i= input("faktoriyelini bulmak istediğiniz sayı:")
    if(i == "q"):
        print("program sonlandırılıyor......")
        break
    else:
        i = int(i)
        faktoriel = 1
        for a in range(2,i+1):
            faktoriel *= a
        print("{} faktoriyel = {}".format(i, faktoriel))
