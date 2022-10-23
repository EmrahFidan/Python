# kullanıcı girişi

print(""""
****************************
KULLANICI GİRİŞİ
****************************
""")

sys_kullanıcı_adı = "emrah"
sys_parola ="12345"

kullanıcı_adı = input("Kullanıcı adı:")
Parola = input("Parola:")

if(sys_kullanıcı_adı == kullanıcı_adı and sys_parola !=Parola):
    print("parola hatalı")
elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola == Parola):
    print("kullanıcı adı hatalı")
elif (sys_kullanıcı_adı != kullanıcı_adı and sys_parola != Parola):
    print("kullanıcı adı ve parola hatalı")
else:
    print("sisteme başarıyla giriş yapıldı")