def test():
    a = ['a', 'b', 'c']
    for idx, i in enumerate(a):
        print("%d - %s" % (idx, i))


class TestClass:

    def __init__(self):
        self.deneme_degeri = 1

    def topla(self, a, b):
        """
        Bu bir test sınıfıdır.

        :param a: Toplama işlemi için ilk sayı.
        :type a: int
        :param b: Toplama işlemi için ikinci sayı.
        :type b: int
        :return: İki sayının toplamı.
        :rtype: int
        """
        return a + b


if __name__ == "__main__":
    test_class = TestClass()
    test_class.topla(1, 2)
