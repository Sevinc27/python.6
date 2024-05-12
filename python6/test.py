class Hesab:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans
    def balans_artir(self, miqdar):
        self.balans += miqdar
    def pul_cixar(self, miqdar):
        if miqdar <= self.balans:
            self.balans -= miqdar
        else:
            print("balans kifayet qeder deyil.")
    def balans_goster(self):
        print(f"hesab №{self.hesab_nomresi} - Balans: {self.balans}")
class KreditHesabi(Hesab):
    def __init__(self, hesab_nomresi, balans, kredit_meblegi):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi
    def kredit_ver(self):
        self.balans += self.kredit_meblegi
    def kredit_odenisi(self):
        ayliq_odenis = self.kredit_meblegi / 12
        self.balans -= ayliq_odenis
        print("kredit odenisi ugurla heyata kecirildi.")

hesab1 = Hesab("12568", 800)
hesab1.balans_goster()

hesab1.balans_artir(400)
hesab1.balans_goster()

hesab1.pul_cixar(200)
hesab1.balans_goster()

kredit1 = KreditHesabi("12568", 1000, 800)
kredit1.balans_goster()

kredit1.kredit_ver()
kredit1.balans_goster()

kredit1.kredit_odenisi()
kredit1.balans_goster()







