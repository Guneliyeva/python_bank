""" 
İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  
Pul çıxarmaq  və balansı göstərmək üçün metodlar. +
İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  
super initdən  istifadə edəcəyik.   Bu classda bizim 2 metodumuz olacaq. Kredit vermək və
kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.                                                        Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).
"""


class Hesab:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = int(hesab_nomresi)
        self.balans = balans

    def balans_artir(self, pul):
        self.pul = pul
        self.balans += self.pul
        return self.balans

    def pul_cixar(self, pul):
        self.pul = pul
        self.balans -= self.pul
        return self.balans

    def balans_goster(self):
        print(self.balans)


account1 = Hesab(1234, 300)
account1.balans_goster()
print(account1.balans_artir(50))
print(account1.pul_cixar(30))


class Kredit(Hesab):
    def __init__(self, hesab_nomresi, balans, mebleg):
        self.mebleg = mebleg        
        super().__init__(hesab_nomresi, balans)

    def kredit_ver(self):
        self.balans+=self.mebleg  
        return self.balans

    def kredit_ode(self,ay):
        self.ay=ay
        ayliq_mebleg=self.mebleg/ay
        while self.mebleg>0:
            self.mebleg-=ayliq_mebleg
            qalan_mebleg=self.mebleg
            print(qalan_mebleg)
           

kredit=Kredit(1234,500, 2500)  
ay=kredit.kredit_ode(5)
kredit.kredit_ver()
print(f"Kreditin meblegi {kredit.mebleg}, odeceyiniz ay muddeti {kredit.ay}") 
#kredit meblegini nece duzgun cagira bilerem? sehv yazmisam tapa bilmedim oyrenmek isteyirem




