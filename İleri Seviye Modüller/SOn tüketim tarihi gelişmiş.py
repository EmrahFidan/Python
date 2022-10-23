from datetime import datetime

yıl = int(input("son tüketim tarihi yılı:"))
ay = int(input("son tüketim tarihi ayı:"))
gün = int(input("son tüketim tarihi günü:"))

tarih = datetime(yıl,ay,gün)

bugün = datetime.now()

STK = tarih - bugün

print(STK.days, "gün sonra bitecek")

