class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.number = L

    def __str__(self):
        return str(self.number)

    __repr__ = __str__

    def __len__(self):
        return len(self.number)


f = Fib(10)
print f
print len(f)
