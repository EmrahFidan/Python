class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding= "utf-8") as file:

            dosya_icerigi = file.read()
          #  print(dosya_icerigi)

            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler =list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
        #    for i in self.sade_kelimeler:
            #      print(i)
    def tum_kelimeler(self):

        kelimeler_kumesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)

        print("Tüm Kelimeler.....")

        for i in kelimeler_kumesi:
            print (i)

    def kelime_frekansı(self):

        kelime_sözlük = dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sözlük):

                kelime_sözlük[i] +=1

            else:
                kelime_sözlük[i] = 1

        for kelime,sayı in kelime_sözlük.items():

            print("Kelime: {} , Tekrarı :{}".format(kelime,sayı))

    def kelime_bul(self):
        while(1):
            ara = input("Aramak istediğiniz kelimeyi giriniz: ")

            if ara in self.sade_kelimeler:
                print("{} kelimesi {} defa geçiyor...".format(ara,self.sade_kelimeler.count(ara)))

            else:
                print("aradığınız kelime bulunmamaktadır.")

            a = input("çıkmak istiyorsanız 'q' tuşuna basınız // devam etmek istiyorsanız herhangi bir tuşa basabilirsiniz !!")
            if (a == "q"):
                break
            else:
                continue



dosya = Dosya()

dosya.tum_kelimeler()

# dosya.kelime_frekansı()

# dosya.kelime_bul()

"""
ilk önce metnimize erişmek için dosyamızı açıyoruz.
sınıf (class) içinde yazmamızın sebebi daha sonra başka yerlerde de kullanabilmek.
dosyayı okuyoruz.
sonrasında split kullanrak metinde kullanılan tüm boşluklardan kelimeleri birbirinden ayırıyoruz.
sadeleştirdiğimiz her kelimeyi yeni bir listeye atmak için boş liste oluşturuyoruz.
sade kelimeler listesindeki her kelimeden bir tane olması için boş bir küme oluşturup kümeler 
üzerinde işlemler yapacağız.
bir kelimeden kaç tane geçtiğini bulmak için kelime frekansı fonksiyonu oluşturuyoruz.
"""