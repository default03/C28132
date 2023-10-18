from time import sleep
from random import choice
class StudentLife:
    def __init__(self, name:str, age:int):
        self.Age = age
        self.Name = name
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n")
    def start(self):
        Ovrsght = 0 # Замечания
        Hngr = 100 # Голод
        ANSW=0 # Счетчик правильных ответов экзамена
        answ = "" # Остальные ответы
        IsWin = True # Итоговое значение
        DaysOfFood = [7,14,21,28,35,42,49,56,63,70,77,84,91,98] # Дни принятия еды
        IsDie = [1,0,0,0,1,0,0,1,0,0] # 1 - отрава,смерть 30%
        i = 0
        while i < 100:
            # Проверка значения ЗАМЕЧАНИЯ
            if Ovrsght==2:
                print("You're excluded!\n")
                IsWin = False
                break
            # Проверка значения ГОЛОДА
            if Hngr<=0:
                print("You died!\n")
                IsWin = False
                break
            i+=1
            # Вывод основной информации
            print("-------------------------------\n"
                  f"Day {i}\n"
                  f"Oversights - {Ovrsght}\n"
                  f"Hunger - {Hngr}%\n"
                  "-------------------------------\n\n")
            Hngr-=7
            # Проверка прошла ли одна неделя для принятия еды
            for j in DaysOfFood:
                if (i==j):
                    # Вывод вопроса и доп.информации
                    if (Hngr<=49):
                        eat = input("Will eat? (y/n) (You will die if you don't eat now!!!)\nAnswer: ")
                    else:
                        eat = input("Will eat? (y/n)\nAnswer: ")
                    # Проверка значения ответа
                    if eat == 'y' or eat == 'Y':
                        # 30% шанс выпадения просроченной еды
                        badfood = choice(IsDie)
                        if badfood==1:
                            Hngr = 100
                            print("You ate poor quality food " # Предупреждение
                                  "You have been poisoned!\n\n"
                                  "1. Continue (chance to die 30%)\n" # Шанс смерти 30%
                                  "2. Skip school (+Oversight)") # +замечание за пропуск
                            while True:
                                answ = input("\nAnswer (1/2): ")
                                if (answ=='1' or answ=='2'):
                                    break
                            if answ=="1":
                                die = choice(IsDie) # Шанс смерти 30%
                                if die==1:
                                    IsWin = False
                                    break
                            else:
                                Ovrsght+=1
                        else:
                            Hngr = 100
            # Экзамен
            if i==30 or i==60 or i==90:
                print("Today exam!\n"
                      "Question\n"
                      "1. 35 * 2\n"
                      "2. 43 + 7\n"
                      "3. √9-4√5\n\n ANSWERS")
                a1 = input("1. ")
                a2 = input("2. ")
                a3 = input("3. ")
                if a1=="70":
                    ANSW+=1
                if a2=="50":
                    ANSW+=1
                if a3=="i dont know":
                    ANSW+=1
                if ANSW<2:
                    print("You failed exam! +Oversight\n\n")
                    Ovrsght+=1
                    sleep(3)
                if ANSW>=2:
                    print("Congratulations! You passed the exam\n\n")
                    sleep(3)
            sleep(0.4)
        # Итоги
        if IsWin==True:
            print("\n\n==========================================================\n"
                  "=======================  YOU WIN  ========================\n"
                  "==========================================================")
        else:
            print("\n\n==========================================================\n"
                  "=======================  YOU LOST  =======================\n"
                  "==========================================================")


