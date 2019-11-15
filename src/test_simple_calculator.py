import simpleCalculator as calculator
def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(-1,-1) == -2
    assert calculator.add(4,5) == 9
    assert calculator.add(1,2,3,4) == 10
    assert calculator.add(0,1) == 1
    assert calculator.add(-100,10) == -90
def test_multiply():
    assert calculator.multiply(1,2) == 2
    assert calculator.multiply(1,2,3,4) == 24
    assert calculator.multiply(-100,10) == -1000
    assert calculator.multiply(-3,-4) == 12
    assert calculator.multiply(0,1,2,3) == 0
