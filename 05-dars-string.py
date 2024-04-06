# 05-dars. string ian ishlash
# Vaqt: 31.03.2024 9:02
# o'rganuvchi Muhammadjon Ahmadov

#meva = "      olma    "
#print("men"+meva.lstrip() + "yaxshi ko'raman")
#print("men"+meva.rstrip() + "yaxshi ko'raman")
#print("men"+meva.strip() + "yaxshi ko'raman")

ism= input("ismingiz nima?\n>>>") #ismini keyinga qatorga o'tkazarkan
#print("assalomu alaykum,", ism.title())
# Vazifalar
#kocha="bog'bon"
#mahalla = "sog'bon"
#tuman = "bodomzor"
#viloyat = "samarqand"

viloyat=input("qaysi viloyatdansiz? \n>>")
tuman = input("tumaningiz qaysi \n>>")
mahalla = input("qaysi mahhallada turasiz? \n>>")
kocha = input("qaysi ko'chada istiqomat qilasiz \n>> ")
print(ism.title(), viloyat.capitalize(), "viloyati,",tuman.title(), "tumani,",mahalla.title(), "mahallasi,", kocha.title(), "ko'chasida istiqomat qiladi")
#print(viloyat.capitalize(), "viloyati,",tuman.title(), "tumani,",mahalla.title(), "mahallasi,", kocha.title(), "ko'chasi")
manzil = f"{viloyat} {tuman} {mahalla} {kocha}"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
