#module\GUI.py

NAME = "GUI"

class Gui:
    border = 0
    inp_ok = False

    def __init__(self, mod = 0):
        self.mod = mod
        print('BookingMaster is started!')

    def inp(self, mass1, mass2):
        a = len(mass1)
        b = len(mass2)
        print(f" {"группа_1":<20} ", end='')
        print(f" {"группа_2":<20} ")
        for i in range(max(a, b)):
            if i < a and i < b:
                print(f"[{mass1[i]:<20}]", end='')
                print(f"[{mass2[i]:<20}]")
            if i >= a:
                print(f"[{"0":<20}]", end='')
                print(f"[{mass2[i]:<20}]")
            if i >= b:
                print(f"[{mass1[i]:<20}]", end='')
                print(f"[{"0":<20}]")
        while True:
            flag = input("перейти к составлению очереди(yes/no):")
            if flag.lower() == "yes":
                self.inp_ok = True
                return
            if flag.lower() == "no":
                self.inp_ok = False
                return


    def border_master(self, n):
        border = input(f"Введите размер первой группы,\nили нажмите entr чтобы ввести значение по умолчанию({n // 2}); максимум({n}):")
        if border == '':
            self.border = n // 2
            return n // 2
        self.border = n // 2
        return int(border)

    @staticmethod
    def rez(mass):
        for i in mass:
            print(f"[{i:<20}]")

    @staticmethod
    def end():
        print("BookingMaster to end.")