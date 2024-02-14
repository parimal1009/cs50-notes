import seasons
def main():
    test_ans()
def test_ans():
    assert seasons.ans("2021-3-20") == "One million, fifty-one thousand, two hundred"
    assert seasons.ans("2022-3-20") == "Five hundred twenty-five thousand, six hundred"
    assert seasons.ans("2022 march 20") == "Invalid Date"
if __name__ == "__main__":
    main()
