"""
Sana: 01.04.2024 Vaqt: 12:27

08-dars. listlar(davomi)
o'rganuvchi: Muhammadjon Ahmadov
"""
davlatlar = ['Angliya','Fransiya','Avstriya','Bolgariya','Germaniya','Shvetsiya','Italiya','Ispaniya','Portugaliya']
taomlar = ['chuchvara','manti','qozonkabob','osh','somsa']
nonushta = taomlar[:]
nonushta.remove('qozonkabob')
nonushta.remove('chuchvara')
nonushta.append('qaymoq')
nonushta.insert(0,'blinchik')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta = list(nonushta)

nonushta.insert(0,'non va qaymoq')
nonushta = tuple(nonushta)
print(nonushta)
