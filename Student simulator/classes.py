from time import sleep
class StudentLife:
    Ovrsght = 0
    Hngr = 100
    IsDie = False
    def __init__(self, name:str, age:int):
        self.Age = age
        self.Name = name
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n")
    def days(self):
        Ovrsght = 0
        Hngr = 100
        IsDie = False
        for i in range(0,100):
            if Ovrsght>2:
                print("You're excluded!\n")
                IsDie = True
                break
            if Hngr<0:
                print("You died!\n")
            i+=1
            ANSW=0
            print(f"Day {i}\n"
                  f"Oversights - {Ovrsght}\n"
                  f"Hunger - {Hngr}%\n"
                  "-------------------------------")
            Hngr-=6
            if (i==15,i==30,i==45,i==60,i==75,i==90):
                a = input("Will eat? (Y/N)\nAnswer: ")
                print(a)
                if a == "Y":
                    Hngr += 50
            if i==30 or i==60 or i==90:
                print("Today exam!\n"
                      "Question\n"
                      "1. 35 * 2\n"
                      "2. 43 + 7\n"
                      "3. √9-4√5\n\n ANSWERS")
                a1 = input("1. \n")
                a2 = input("2. \n")
                a3 = input("3. \n")
                print(a1,a2,a3)
                if a1=="70":
                    ANSW+=1
                if a2=="50":
                    ANSW+=1
                if a3=="i dont know":
                    ANSW+=1
                if ANSW<2:
                    print("You failed exam! +Oversight")
                    Ovrsght+=1
        if (IsDie==True):
            "\n---------- YOU FAILED ------------"



