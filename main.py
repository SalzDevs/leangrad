class Operation:
    def __init__(self,var1,var2,oper):
        self.var1 = var1
        self.var2 = var2
        self.oper = oper

    def __str__(self):
        return f"{self.var1} {self.oper} {self.var2}"

class Value:
    def __init__(self,data:int,varName:str):
        self.data = data
        self.operations = []
        self.varName = varName


    def add(self,val1, val2):
        operation = Operation(val1.varName,val2.varName,"+")
        self.operations.append(str(operation))
        self.data = val1.data+val2.data

    def mul(self,val1,val2):
        #self.operations.append()str(val1.data) + "-" + str(val2.data))
        #self.data = val1.data*val2.data
        pass
    def sub(self,val1,val2):
        #self.operations.append(str(val1.data) + "-" + str(val2.data))
        #self.data = val1.data-val2.data
        pass

#init (x,y,z)
x = Value(7,'x')
y = Value(3,'y')
z = Value(0,'z') 

#operations on z
z.add(x,y)

print(z.data)
print(z.operations)
