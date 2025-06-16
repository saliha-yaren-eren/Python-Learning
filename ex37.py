#ex37
kl=[1,2,3,4,5,6,7,8,9]
del kl[2]
print(kl)
jk=[1,2,3,4,5,6,7,8,9]
del jk[1:2]
print(jk)
mk={'a':1, 'b': 2}
del mk['a']
print(mk)
keys=mk.keys()
print(keys)
print(mk.values())
print(mk.items())
print(mk.get('b'))
mk.update({'b': 5 ,'c': 9})
print(mk)
print(mk.pop('b'))
print(mk)
kl.append(50)
print(kl)
kl.remove(1)
print(kl)
kl.pop(-2)
print(kl)
kl.insert(4,80)
print(kl)
del jk
kl.clear()
print(kl)
hu={1,2,3,4,5}
hu.add(7)
print(hu)
hu.remove(3)
print(hu)
df={5,6,7,8,9}
print(hu.union(df))
print(hu.intersection(df))
metin='hello world'
print(metin.upper())
print(metin.lower())
print(metin.replace('hello', 'hi'))
print(metin.split())

import math as m
from random import randint
sayi=randint(1, 100)
print(f"{sayi} sayısının karekökü {m.sqrt(sayi)}")

try:
    sayi1=int(input("sayı giriniz "))
    sonuc=100/sayi1
    print(sonuc)
except ZeroDivisionError :
    print("Sıfıra bölünme hatası!")

with open("rapor.txt","w") as dosya:
    dosya.write("Python öğreniyorum!")
print("Yazıldı.")

isim=input("isim giriniz ")
print(f"Merhaba {isim}, yaşın 25.")

x=5
def fonk():
    global x
    x=10
fonk()
print(x)

y=5
assert y > 0, "0dan büyük olmalı"
print(y)

def sayilar():
    for i in range(5):
        yield i #return → fonksiyonu tamamen bitirir.
for sayi in sayilar():
    print(sayi)

liste=[1,2,3,4]
print(3 in liste)

class Banka:
    def __init__(self,isim,şifre):
        self.isim=isim
        self.şifre=şifre

    def hesap(self,bakiye,çekilen_tutar):
        if bakiye<çekilen_tutar:
            raise ValueError("Yetersiz Bakiye!")
        else:
            print(f"Sayın {self.isim}. Çekilen tutar {çekilen_tutar}, kalan bakiye {bakiye-çekilen_tutar}")
try:
    kullanici=Banka(input("Please enter your name! "), input("Please enter your password! "))
    kullanici.hesap(1000,int(input("Please enter money amount that you want ")))
except ValueError as hata:
    print(hata)
finally:
    print("İşlem bitti.")
print("Tekrar deneyiniz!")

kod="print('Merhaba')"
exec(kod)

for i in range(5):
    if i==2:
        continue
    print(i)

a=[1,2,3]
b=a
print(a is b) #is: aynı nesne mi?
print(a == b) #==: değerler aynı mı?

kare= lambda x: x**2
print(kare(4))

print("Merhaba\fDünya\vNaber")
