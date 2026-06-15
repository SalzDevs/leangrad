class Value:
    def __init__(self,data:int):
        self.data = data
        self.operations = []


    def add(self,val1, val2):
        self.operations.append(str(val1.data) + "+" + str(val2.data))
        self.data = val1.data+val2.data

    def mul(self,val1,val2):
        self.operations.append(str(val1.data) + "*" + str(val2.data))
        self.data = val1.data*val2.data

x = Value(7)
y = Value(3)

z = Value(0) 
z.add(x,y)
z.add(z,Value(1))
z.mul(z,Value(2))

print(z.data)
print(z.operations)
