#soal inheretance
#1. Lengkapi syntax berikut!
#2. Tambahkan atribut namadepan, namabelakang dan umur pada kucing!
#3. Gunakan Overriding pada Kucing, menggunakan method nama yang dimiliki Hewan!
#4. Berikan Output untuk Kucing! contoh: kucing persia umur 30 tahun

class Hewan:
    def __init__(self, depan, belakang):
        self.depan = depan
        self.belakang = belakang
    def __str__(self):
        return self.depan + " " + self.belakang
		
class Kucing(Hewan):
    def __init__(self, depan, belakang, umur):
        super().__init__(depan, belakang)
        self.umur = umur
    def __str__(self):
        return super().__str__() + " " + "umur" + " " + self.umur + " " + "tahun"

#NB : Lihat file sebelumnya untuk menjawab, bisa copas. Berbeda lebih baik

k = Kucing("Kucing","Persia","30")
print(k)