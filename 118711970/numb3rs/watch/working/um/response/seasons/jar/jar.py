class Jar:
    def __init__(self, capacity=12):
        self.capacity1 = capacity
        self.size1 = 0
        if(capacity < 0):
            raise ValueError
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity or (n + self.size > self.capacity):
            raise ValueError
        self.size1 += n
    def withdraw(self, n):
        if n  > self.size:
            raise ValueError
        self.size1 -= n
    @property
    def capacity(self):
        return self.capacity1
    @property
    def size(self):
        return self.size1
def main():
    a = Jar(4)
    a.deposit(3)
    a.withdraw(4)
    print(a.capacity)
    print(a.size)
if __name__ == "__main__":
    main()
