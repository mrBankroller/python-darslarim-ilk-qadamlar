"""
01.04.2024
07-dars. listlar
vaqt:10:11
"""
"""# O'TILGANLARI
mevalar= ['nok','olma','anor','apelsin',"o'rik", 'banan']
sonlar = [2005, 3658, 45200, 41540, 9800 ,19780]
#print(mevalar[0])
#print(sonlar[2])
#print(sonlar[-2])
#print("birinchi meva:",mevalar[0].title())
#print("oxirgi meva:\n",mevalar[-1].capitalize())
mevalar.append('lacetti')
mevalar.insert(0,'sabzi')
#print(mevalar)
mevalar.insert(-1, "uzum")
#print(mevalar)
cars = []
cars.append('matiz')
cars.append('lacetti')
cars.append('damas')
cars.append('malibu')
cars.append('spark')
cars.append('mercedes')
del cars[3]
cars.insert(0, 'vaz2107')
cars.insert(-1, 'vaz2107')
jiguli = cars.pop()
#print(f'men {jiguli} rusumli mashina sotib oldim')
#print("olmoqchi bo'lgan mashinalarim: ",cars)"""

# VAZIFALAR
""" # VAZIFA 1
ismlar = []
ismlar.append("Zafar")
ismlar.append('Shahzod')
ismlar.append("Ulug'bek")
ismlar.append("Bekzod")
ismlar.append("Salohiddin")
print(f"Salom, {ismlar[0]}, bugun choyxona bormi?")
print(f"{ismlar[1]}, boks tushamiz")
print(f"{ismlar[2]}, qachon qarzingni berasan?")
print(f"{ismlar[3]}, slayd qilib bering")
print(f"{ismlar[4]}, ko'rinmay kettiz, oshna")
"""
""" # VAZIFA 2
sonlar = []
sonlar.append(325)
sonlar.append(-346.4)
sonlar.append(3059.6)
sonlar.append(-521)
sonlar.append(12.5)
sonlar[1] =sonlar[1]**2
sonlar[3] = (-1)*sonlar[3]
sonlar[4]  = sonlar[4]/55
sonlar[3] = sonlar[3]//55
print(sonlar[3]+sonlar[4])
del sonlar[4]
sonlar.remove(325)
sonlar[0] = sonlar[0]//1
print(sonlar.pop(2))
sonlar.append(45.35)
sonlar.append(123.025)
sonlar.insert(1, -654)
sonlar[1] =sonlar[1]**2
sonlar[3] = (-1)*sonlar[3]
sonlar[4]  = sonlar[4]/55
sonlar[3] = sonlar[3]//55
print(sonlar[3]+sonlar[4]) """
""" # VAZIFA 3
t_shaxslar = ["Imom Buxoriy",'Al-Zamaxshariy','Umar ibn Xattob','Abu Bakr Siddiq']
z_shaxslar = ['Robert kiyosaki','Shohina','Nozima','Shahnoza']
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan {z_shaxslar.pop(0)} bilan suhbat qilishni hohlar edim") 
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan {z_shaxslar.pop(0)} bilan suhbat qilishni hohlar edim")
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan {z_shaxslar.pop(0)} bilan suhbat qilishni hohlar edim")
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan {z_shaxslar.pop(0)} bilan suhbat qilishni hohlar edim")
"""
"""# VAZIFA 4
friends = []
friends.append("Zafar")
friends.append('Shahzod')
friends.append("Ulug'bek")
friends.append("Bekzod")
friends.append("Salohiddin")
friends.remove('Zafar')
friends.remove('Bekzod')
friends.insert(0, 'Adham')
friends.insert(3, 'Umid')
friends.insert(-1, 'Iroda')
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
print(mehmonlar)
"""