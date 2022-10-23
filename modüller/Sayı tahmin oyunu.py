# rondom ve time modülüyle sayı tahmin oyunu

import random
import time

print("""
************************************
SAYI TAHMİN OYUNU

1 ile 40 arasında sayıyı tahmin edin
************************************
""")

rastgele = random.randint(1,40)
tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele):
        time.sleep(1)
        print("Daha yüksek bir sayı girin:")
        tahmin_hakkı -=1

    elif (tahmin > rastgele):
        time.sleep(0.5)
        print("Daha düşük bir sayı girin:")
        tahmin_hakkı -=1

    else:
        time.sleep(1)
        print("congrculations !!")
        break
    if (tahmin_hakkı == 0):
        print("tahmin hakkınız bitti....")
        print("sayı:",rastgele)
        break
