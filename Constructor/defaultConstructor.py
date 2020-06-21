class Calculator:
    num = 100
    #default contructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber =b
        print("this is default constructor")
#    Executing method in a class
    def sum(self):
        print("Executing method in a class")
    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3)
obj.sum()
print(obj.summation())


obj = Calculator(4,5)
obj.sum()
print(obj.summation())