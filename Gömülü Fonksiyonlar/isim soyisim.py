"""
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
"""
name =  ["Emrah","Yağmur Ebru","Vakkas ","Mustafa Kemal","Özgür","Ahmet","Yiğit Emre","Polat"]
surname = ["Fidan","Fidan","Karakurt","Atatürk","Uysal","Kök","Ünlü","Alemdar"]

for i,j in zip(name,surname):
    print(i,j)