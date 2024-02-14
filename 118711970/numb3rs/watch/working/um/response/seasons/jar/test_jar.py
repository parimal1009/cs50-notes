from jar import Jar
def test_init():
    a = Jar(2)
    assert a.capacity == 2
    assert a.size == 0
    b = Jar()
    assert b.capacity == 12
def test_str():
    a = Jar()
    assert str(a) == ""
    a.deposit(2)
    assert str(a) == "🍪🍪"
    a.deposit(5)
    assert str(a) =="🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    a = Jar()
    a.deposit(4)
    assert a.size == 4
    a.deposit(4)
    assert a.size == 8
    a.deposit(4)
    assert a.size == 12

def test_withdraw():
    a = Jar()
    a.deposit(12)
    a.withdraw(4)
    assert a.size == 8
    a.withdraw(5)
    assert a.size == 3
    a.withdraw(1)
    assert a.size == 2
