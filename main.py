class Value:
    def __init__(self,data:int):
        self.data = data
        self.operations = []


def add(val1:Value, val2:Value) -> Value:
    return Value(val1.data+val2.data)

x = Value(7)
y = Value(3)

z = add(x,y)

print(z.data)
