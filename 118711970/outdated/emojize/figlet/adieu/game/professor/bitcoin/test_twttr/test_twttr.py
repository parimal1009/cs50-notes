import twttr
def main():
    test_twttr()
def test_twttr():
    assert twttr.shorten("hello") =="hll"
    assert twttr.shorten("HELLO") =="HLL"
    assert twttr.shorten("hello, WORLD") =="hll, WRLD"
    assert twttr.shorten("Ankit 13") == "nkt 13"
    assert twttr.shorten(",.;")==",.;"
if __name__ == "__main__":
    main()
