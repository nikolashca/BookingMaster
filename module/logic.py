#module\logic.py
from random import randint
import pandas as pd

NAME = "logic"




def open_grup(gui):
    '''
    эта функция считывает имена из файла glav_grups.xlsx
    и записывает имена до индекса border включительно 
    в массив grup_1, а остальные в мвссив grup_2
    '''
    df = pd.read_excel('glav_grups.xlsx')
    names = df.iloc[:, 0].tolist()

    border = gui.border_master(len(names))

    grup_1 = names[:border]
    grup_2 = names[border:]
    return grup_1, grup_2


def open_memory():
    '''
    эта функция считывает имена из файла output.xlsx
    '''
    df = pd.read_excel('output.xlsx', header=None)
    iter = 0
    names = df.iloc[:, 0].tolist()
    return names


def write_random_queue_to_exel(mass: list, filepath: str = "output.xlsx"):
    """
    Записывает массив data в первый столбец Excel-файла filepath.
    Каждый элемент массива становится значением отдельной ячейки
    в столбце A: A1, A2, A3, ...
    """
    df = pd.DataFrame(mass)          # список → DataFrame (N строк, 1 столбец)
    df.to_excel(filepath, index=False, header=False)
    return mass


def randomeiser(mass):
    '''эта функция перемешивает именна в массиве mass'''
    mixer = []
    mass_end = []

    for i in range(len(mass)):
        mixer.append(i)
    
    while len(mixer) > 0:
        a = mixer.pop(randint(0, len(mixer) - 1))
        mass_end.append(mass[a])
    
    return mass_end

def trigger(mass1, mass2):
    a = len(mass1)
    b = len(mass2)
    if a != b:
        return True
    
    for i in range(a):
        if mass1[i] == mass2[i]:
            return False
        
    return True


def sub_logic(grup_1, grup_2, gui):
    flag = False
    while not flag:
        rand_grup_1 = randomeiser(grup_1)
        rand_grup_2 = randomeiser(grup_2)
        rand_grup = rand_grup_1 + rand_grup_2
        memory = open_memory()
        border = gui.border
        
        memory_grup_1 = memory[:border]
        memory_grup_2 = memory[border:]
        memory = memory_grup_2 + memory_grup_1
        print('1', memory)
        print('2', rand_grup)
        flag = trigger(rand_grup, memory)
    
    random_queue = write_random_queue_to_exel(rand_grup)
    return random_queue


def start_logic(gui):
    while not gui.inp_ok:
        grup_1, grup_2 = open_grup(gui)

        gui.inp(grup_1, grup_2)

    x = 0
    while True:
        x = int(input("введите номер группы которя будет первой в очереди(1 или 2)"))
        if x == 1:
            random_queue = sub_logic(grup_1, grup_2, gui) 
            break
        elif x == 2:
            random_queue = sub_logic(grup_2, grup_1, gui) 
            break
        else:
            print('ошибка ввода!')
   
    gui.rez(random_queue)


