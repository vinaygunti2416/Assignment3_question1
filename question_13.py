class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition :-", self.num1+self.num2)
    def subtract(self):
        if self.num1<self.num2:
            print( "Subtract:-",self.num2-self.num1)
        else:
            print("Subtract", self.num1-self.num2)
    def multiply(self):
        print("Multiply :-" ,self.num1*self.num2)
    def divide(self):
        if self.num1<self.num2:
            print("Division :-", self.num2/self.num1)
        else:
            print("Division :-", self.num1/self.num2)
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
print(f"the first number:-{num1}\nThe second number {num2}")
obj = Calculator(num1 , num2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()