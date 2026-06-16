class Value:
    def __init__(self, data, _prev=(), op=""):
        self.data = data
        self._prev = set(_prev)
        self.op = op
        self.grad = 0
        self._backward = lambda: None

    def add(self, other):
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def mul(self, other):
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def print_graph(self, indent=0):
        print("  " * indent + f"{self.data} [{self.op}]")
        for parent in self._prev:
            parent.print_graph(indent + 1)

x = Value(7)
y = Value(3)

z = x.add(y)
z = z.add(Value(1))
z = z.mul(Value(2))
z = z.sub(Value(1))

z.print_graph()
