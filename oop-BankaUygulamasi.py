class BankaHesabi:
    def __init__(self,isim,bakiye=0):
        self.isim=isim
        self.bakiye=bakiye

    def para_yatir(self,miktar):
        if miktar>=0:
            self.bakiye+=miktar
            print(f"Yatirilan para sonucunda {self.isim} adli kisinin mevcut bakiyesi : {self.bakiye}")
        else:
            print(f"Yatirilan para sifir veya negatif olamaz!")

    def para_cek(self,miktar):
        if miktar>0:
            if self.bakiye>=miktar:
                self.bakiye-=miktar
                print(f"Cekilen para sonucunda {self.isim} adli kisinin mevcut bakiyesi : {self.bakiye}")
            else:
                print(f"Yeterli bakiyeniz bulunmamaktadir! Mevcut bakiyeniz : {self.bakiye}")
        else:
            print(f"Cekilen para sifir veya negatif olamaz!")

    def para_transferi(self,alici_hesap,miktar):
        if miktar>=0:
            if self.bakiye>=miktar:
                self.bakiye-=miktar
                alici_hesap.para_yatir(miktar)
                print(f"{self.isim} adli kisi {miktar} TL tutarinda {alici_hesap.isim} adli kisiye para transferi gerçekleştirdi") 
                print(f"Transfer sonucunda {alici_hesap.isim} adli kisinin mevcut bakiyesi {alici_hesap.bakiye} TL'dir")
                print(f"Transfer sonucunda {self.isim} adli kisinin mevcut bakiyesi {self.bakiye} TL'dir")
            else:
                print(f"Bakiyeniz işlem için yetersizdir! Mevcut bakiyeniz : {self.bakiye} TL'dir")
        else:
            print(f"Transfer tutari sifir veya negatif olamaz!")

    def mevcut_bakiye(self):
        return (f"{self.isim} adli kişinin mevcut bakiyesi: {self.bakiye} TL'dir")

hesap1=BankaHesabi("Emma",4000)
hesap2=BankaHesabi("Aty",4000)

hesap1.para_yatir(1500)
hesap1.para_cek(500)
hesap1.para_transferi(hesap2,2000)

print(hesap1.mevcut_bakiye())
print(hesap2.mevcut_bakiye())