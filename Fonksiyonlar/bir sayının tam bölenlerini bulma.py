# kullanıcıdan alınan bir sayının tam bölenlerini bulup yazdıran program
liste=[]
def tam_bölenler(x):
    if(x == 0):
        return False
    else:
        global liste
        for i in range(1,x+1):
            if(x % i == 0):
                liste.append(i)
        return liste


while True:
    x = input("enter a number: ")
    if(x == "q"):
        break
    else:
        x = int(x)
        if(not tam_bölenler(x)):
            print("girilen sayının tam böleni yoktur.")
        else:
            print("sayının tam bölenleri:",liste)
            liste = []
