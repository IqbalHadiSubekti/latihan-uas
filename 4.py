#Abstract
#1. Apa yang dimaksud abstract class dan abstract method?
#2. Apa hubungan abstract dengan inheretance?
#3. Apakah implementasi abstract hanya dapat dilakukan pada subclass?
#4. Bagian yang menunjukan abstract?
#5. Berikan output untuk pertambahan! contoh: 10

from abc import ABC, abstractmethod
class Operasi(ABC):
    def __init__(self, angka_1, angka_2):
        self.angka_1 = angka_1
        self.angka_2 = angka_2
        super().__init__()
        
    @abstractmethod
    def eksekusi(self):
        pass

class Pertambahan (Operasi):
    def eksekusi(self):
        return self.angka_1 + self.angka_2
		
p = Pertambahan(2,3)
print(p.eksekusi())
