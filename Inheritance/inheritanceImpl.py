from defaultConstructor import Calculator

class childImpl(Calculator):
    num2 = 500


    def __init__(self):
        Calculator.__init__(self,5,6)

    def getCompleteData(self):
        return self.summation() + self.num + self.num2

obj2 = childImpl()
print(obj2.getCompleteData())

 

           