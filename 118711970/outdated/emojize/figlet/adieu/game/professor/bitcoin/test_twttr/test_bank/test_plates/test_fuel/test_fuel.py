import fuel
def main():
    test_convert()
    test_gauge()
def test_convert():
    assert fuel.convert("5/8") == 62
    assert fuel.convert("1/4") == 25
    assert fuel.convert("4/4") == 100
    assert fuel.convert("0/4") == 0
    assert fuel.convert("3/4") == 75
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1
def test_gauge():
    assert fuel.gauge(62) == '62%'
    assert fuel.gauge(25) == '25%'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
if __name__ == "__main__":
    main()
