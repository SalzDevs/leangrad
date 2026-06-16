class Value:
    def __init__(self, data, _prev=(), op=""):
        self.data = data
        self._prev = set(_prev)
        self.op = op
        self.grad = 0
        self._backward = lambda: None

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    def __mul__(self, other):
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

z = x + y
z = z + Value(1)
z = z + Value(2)
z = z + Value(-1)
z = z * z

z.print_graph()
