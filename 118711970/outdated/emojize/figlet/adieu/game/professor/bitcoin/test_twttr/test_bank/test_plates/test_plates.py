import plates
def main():
    test_is_valid()
def test_is_valid():
    assert plates.is_valid("MOON") == True
    assert plates.is_valid("AA22AA")== False
    assert plates.is_valid("abc123")== True
    assert plates.is_valid("HELLO, WORLD") == False
    assert plates.is_valid("1234hello") == False
    assert plates.is_valid("a") == False
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("50") == False
    assert plates.is_valid("AA,22") == False
    assert plates.is_valid("H")== False
if __name__ == "__main__":
    main()
