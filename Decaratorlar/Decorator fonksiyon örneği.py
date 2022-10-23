def ekstra(func):

    def wrapper(sayılar):

        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:

            if(sayı % 2 == 0):
                çiftler_toplamı += sayı
                çift_sayılar += 1

            else:
                tekler_toplamı += sayı
                tek_sayılar += 1

        print("Teklerin ortalaması : ",tekler_toplamı / tek_sayılar)
        print("çiftlerin ortalaması : ",çiftler_toplamı / çift_sayılar)

        func(sayılar)
    return wrapper

@ekstra
def ortalama_bul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam += sayı

    print("Genel Ortalama: ",toplam/len(sayılar))


ortalama_bul([1,2,3,4,34,60,63,32,100,105])