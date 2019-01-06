#Inheretance Overriding dan Overloading
#1. Apa itu Overriding?
#2. Bagian yang menunjukan Overriding? jelaskan!
#3. Berikan output untuk pegawai! contoh: Pain Akatsuki NIP 1995

class Orang:
    def __init__(self, depan, belakang):
        self.depan = depan
        self.belakang = belakang
    def __str__(self):
        return self.depan + " " + self.belakang

class Pegawai(Orang):
    def __init__(self, depan, belakang, NIP):
        super().__init__(depan, belakang)
        self.NIP = NIP
    def __str__(self):
        return super().__str__() + " " + "NIP" + " " + self.NIP
		
a = Pegawai("Pain","Akatsuki","1995")
print(a)