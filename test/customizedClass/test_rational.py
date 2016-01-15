class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        if self.p < self.q:
            k = self.p
        else:
            k = self.q
        for x in range(k, 0, -1):
            if self.p % x == 0 and self.q % x == 0:
                self.p /= x
                self.q /= x
                break
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
