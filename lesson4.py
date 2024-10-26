print("LESSON4!")


class Group:
    name: str
    qty_student: int
    isOnline: bool

    def __init__(self):
        self.group_name = 'C2117'
        self.qty_student = 21
        self.isOnline = True


class HarazhaMakar(Group):
    first_name: str
    second_name: str
    age: int

    def __init__(self):
        Group.__init__(self)
        self.first_name = 'Макар'
        self.second_name = 'Гаража'
        self.age = 14

    def get_info(self):
        print(f'date of student: \t{self.first_name + " " + self.second_name} | {self.group_name}')

harazha_makar = HarazhaMakar()
harazha_makar.get_info()

class Group1: #Описання групи
    name: str
    qty_student: int
    isOnline: bool
    teacher_Age = int

    def __init__(self): #Надання значень групі
        self.group_name = "8a"
        self.qty_student = 37
        self.isOnline = True
        teacher_Age = 40


class RatsynIgor(Group): #Група
    first_name: str
    second_name: str
    age: int

    def __init__(self): #Надання значень групи
        Group.__init__(self)
        self.first_name = 'Ігор'
        self.second_name = 'Рацин'
        self.age = 14

    def get_info(self):
        print(f'date of student: \t{self.first_name + " " + self.second_name} | {self.group_name}')
        print(f'age of student: \t{self.age + " " + self.teacher_Age}')
        #Формутавання рядка за допомогою f можна вивести змінну в рядок з текстом

ratsyn_igor = RatsynIgor()
ratsyn_igor.get_info()
