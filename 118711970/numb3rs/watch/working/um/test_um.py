import um
def main():
    test_count()
def test_count():
    assert um.count("um") == 1
    assert um.count("um?") == 1
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um, thanks, um...") == 2
if __name__ == "__main__":
    main()
