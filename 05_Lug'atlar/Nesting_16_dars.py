# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 07:36:58 2022

@author: Ogabek
"""

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }


car = car0
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")  
  
  

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    

print(cars[0])
print(cars[0]['model'])

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
    

# # # LUG'AT ICHIDA RO'YXAT

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')
        

# # # LUG'AT ICHIDA LUG'AT

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }


for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
       # AMALIYOT

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona"
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot"
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    tjoy = shaxs['tjoy']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")
    
    

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)


