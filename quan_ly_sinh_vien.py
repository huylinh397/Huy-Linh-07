
class sinhvien:
    def __init__(self):
        self.name = input('nhập họ và tên: ')
        self.id_sv = int(input('nhập id_sv: '))
        self.grades = []
    def add_grade(self):
        self.grades.append(float(input('Vào điểm: ')))
        self.grades.append(float(input('Vào điểm: ')))
    def average_grade(self):
        aveage_grade = sum(self.grades)/2
        if aveage_grade < 5:
            kind = "Chưa hoàn thành"
        if aveage_grade >=5:
            kind = "Hoàn thành"
        return [aveage_grade, kind]
        
class quan_ly_sinh_vien: 
    def __init__(self) :
        self.sinhvien = []
    def add_sinhvien(self, sv):
        self.sinhvien.append(sv.__dict__)
    def count_sinhvien(self):
        return len(self.sinhvien)
    def remove_sinhvien(self, id):
        for i in self.sinhvien:
            if i.get("id_sv") == id:
                self.sinhvien.remove(i)
    def show(self):
        print(self.sinhvien)
    def find_sinhvien(self, name):
        for i in self.sinhvien:
            if i.get("name") == name:
                print(i)
    
sv1 = sinhvien()
sv1.add_grade()
sv2 = sinhvien()
sv2.add_grade()
qlsv = quan_ly_sinh_vien()
qlsv.add_sinhvien(sv1)
qlsv.add_sinhvien(sv2)
print(sv1.average_grade())


    


