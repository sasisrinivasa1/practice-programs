class TokenCounter():
    hiddenCount = 0
    def counter(self):
        self.hiddenCount += 1
        return self.hiddenCount

number = TokenCounter()
number.counter()
number.counter()
print(number.counter())