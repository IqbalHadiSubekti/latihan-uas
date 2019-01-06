#Inheretance
#1. Apa yang dimaksud Inheretance?
#2. Bagian yg menunjukan inheretance, superclass, subclass, parent, dan child?
#3. Berikan output untuk orang! contoh: Lebah Ganteng
#4. Perbedaan Pegawai dengan Pegawai_2?
class Orang:
    def __init__(self, depan, belakang):
        self.namadepan = depan
        self.namabelakang = belakang
    def __str__(self):
        return self.namadepan + " " + self.namabelakang

class Pegawai(Orang):
    def __init__(self, depan, belakang):
        super().__init__(depan, belakang)

class Pegawai_2(Orang):
    def __init__(self, depan, belakang):
        Orang.__init__(depan, belakang)

iqbal = Orang("Lebah","Ganteng")
print(iqbal)