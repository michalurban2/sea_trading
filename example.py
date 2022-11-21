class X:
    def __init__(self, value):
        self._value = value

    @property  # getter
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, int):
            raise TypeError('Something is no yes')

        self._value = val


# x = X(42.6)
# x._value = 666
# print(x.value)
# x.value = 42
# print(x.value)


class A:
    @staticmethod
    def magic():
        print('magic a')


class B(A):
    @staticmethod
    def magic():
        print('magic b')


class C(B, A):
    pass


c = C()
c.magic()


class Z:
    def __init__(self, value):
        self.value = value

    def get_uppercase(self):
        return self.value.upper()


class Z1(Z):
    def __init__(self, value):
        super().__init__(value)

    def get_increment(self):
        return int(self.value) + 1


z = Z('ala')
print(z.get_uppercase())

z1 = Z1(42)
print(z1.get_increment())

print(z1.get_uppercase())