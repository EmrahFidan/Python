#liste = ["345","sadas","324a","14","kemal"]
#Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
#Bunu yaparken try,except bloklarını kullanmayı unutmayın.


liste = ["345", "sadas", "324a", "14", "kemal","558484","emrah"]

for eleman in liste:

    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass  # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.