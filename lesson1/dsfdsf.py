class Student:
    def __init__(self, name:str, age:int, group:str, middle:float = None):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Middle = middle
    def __bool__(self):
        return self.Age == None and/
               self.Name == None and/
               self.Group == None and/
               self.Middle == None
    def __len__(self):
        return len(self.Name)
    def __str__(self):
        return (f'Name - {self.Name}\n'
                f'Age - {self.Age}\n'
                f'Group - {self.Group}\n'
                f'Middle - {self.Middle}\n')