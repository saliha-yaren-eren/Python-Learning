"""import os
print("Dosya burada oluşturuluyor:", os.getcwd())

elma_halil=10
elma_veli=10
armut_halil=10
armut_veli=10
line1="Halilin toplam meyve sayisi: %d" % (elma_halil+armut_halil)
line2="Velinin toplam meyve sayisi: %d" % (elma_halil+armut_halil)
dosya_adi="rapor.txt"
acik_rapor=open(dosya_adi, 'w')
acik_rapor.write(line1)
acik_rapor.write("\n")
acik_rapor.write(line2)
acik_rapor.write("\n")
acik_rapor.close()
oku_rapor=open(dosya_adi, 'r')
print(oku_rapor.read())
oku_rapor.close()
elma_halil2=int(input("Halilin aldigi elma sayisi:"))
elma_veli2=int(input("Velinin aldigi elma sayisi:"))
armut_halil2=int(input("Halilin aldigi armut sayisi:"))
armut_veli2=int(input("Velinin aldigi armut sayisi:"))
halil_toplam=elma_halil2+armut_halil2+elma_halil+armut_halil
veli_toplam=elma_veli2+armut_veli2+elma_veli+armut_veli
son_rapor=open(dosya_adi, 'a')
line3="Halilin toplam meyve sayisi: %d" % halil_toplam
line4="Velinin toplam meyve sayisi: %d" % veli_toplam
son_rapor.write(line3)
son_rapor.write("\n")
son_rapor.write(line4)
son_rapor.close()
son_oku_rapor=open(dosya_adi, 'r')
print(son_oku_rapor.read())
son_oku_rapor.close()
basarili=(halil_toplam+veli_toplam>50) * "Başarılı satış"
basarisiz=(halil_toplam+veli_toplam<50) * "Başarısız satış"
print(basarili+basarisiz)"""

