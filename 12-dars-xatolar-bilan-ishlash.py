# -*- coding: utf-8 -*-
"""
12-dars. Xatolar bilan ishlash

sana: 04.04.2024 20:13
o'rganuvchi: Muhammadjon Ahmadov
"""

# son = int(input("Juft son kiriting: "))
# if not son%2==0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat :
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# users = ['alisher1983','aziza','yasina', 'umar']

# login = input("Yangi login tanlang: " )

# if login.lower() in users:
# 	print('Login band, yangi login tanlang!')
# else:
# 	print("Xush kelibsiz!")
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

