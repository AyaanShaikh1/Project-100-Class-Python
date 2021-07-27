class Data :
    def __init__(self,name,age,hobby):
        self.name = name   
        self.age = age
        self.hobby = hobby
    def greet(self) :
        print(f'Hello {self.name}')
obj = Data(input('What is your name? : '),input('What is your age? : '),input('What is your hobby? : '))
obj.greet()        
