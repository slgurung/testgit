import calculator


class TestCalc:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_multi(self):
        assert 6 == calculator.multiply(2, 3)

    def test_sub(self):
        assert 4 == calculator.sub(6, 2)
