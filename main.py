class Value:
    def __init__(self,data:int):
        self.data = data
        self.operations = []


def add(val1:Value, val2:Value) -> Value:
    val = Value(val1.data+val2.data)
    val.operations.append(str(val1.data) + "+" + str(val2.data))
    return val

x = Value(7)
y = Value(3)

z = add(x,y)
z = add(z,Value(1))

print(z.data)
print(z.operations)
