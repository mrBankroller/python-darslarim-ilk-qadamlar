# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti= 0
# if choy: 
#     print("mijoz choy oldi")
#     narx = narx + 3000
# if salat :
#     print("mijoz salat oldi")
#     narx = narx+4500
# if non :
#     print('Mijoz non oldi')
#     narx = narx+4000
# if kompot :
#     print('mijoz kompot oldi')
#     narx= narx+7000
# if assorti :
#     print('mijoz assorti oldi')
#     narx=narx+8000
# print(f"Mijoz {narx} so'm pul to'lashi kerak")

menu = ['osh','manti','qozonkabob','norin','do\'lana','kompyuter']
buyurtmalar = ["manti", 'do\'lana','norin', 'somsa','osh','telefon']
if buyurtmalar:
    for ovqat in buyurtmalar:
        if ovqat.lower() not in menu:
            print(f"bizda {ovqat} yo'q")
        else:
            print(f"{ovqat} buyurtmangiz qabul qilindi.")
    print(f"Rahmat, siz {len(buyurtmalar)} ta ovqat buyurtma qildingiz")
else: 
    print("siz hali buyurtma qilmadingiz")
















