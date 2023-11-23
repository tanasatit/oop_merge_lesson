import random


class Mastermind:
    def __init__(self, color_num, position):
        self.color_num = color_num
        self.position = position
        self.num = 0
        self.rounds = 0
        self.ans = ''
        self.check = ''

    @property
    def color_num(self):
        return self._color_num

    @property
    def position(self):
        return self._position

    @color_num.setter
    def color_num(self, other):
        self._color_num = other

    @position.setter
    def position(self, other):
        self._position = other

    def answer(self):
        for i in range(self.position):
            a = (random.randint(1, self.color_num))
            self.ans += str(a)
        return self.ans

    def check_num(self, ans, guess):
        print(f"Your guess is {guess}")
        list_ans = list(ans)
        remain1 = list(ans).copy()
        remain2 = list(guess).copy()
        for i in guess:
            if i in list_ans:
                if i == list_ans[self.num]:
                    c = '*'
                    self.check += c
                    remain1.remove(i)
                    remain2.remove(i)
            self.num += 1
        remain3 = remain1.copy()
        for j in remain2:
            if j in remain3:
                c = 'o'
                self.check += c
                remain3.remove(j)
        self.rounds += 1
        print(self.check)
        print()
        if self.check != ('*' * self.position):
            self.num = 0
            self.check = ''
        return self.check, self.rounds

    def __str__(self):
        return f"Playing Mastermind with {self.color_num} colors and {self.position} positions"


# main part
x_color = int(input("number of color between 1-8: "))
while x_color > 8:
    x_color = int(input("number of color between 1-8: "))
y_position = int(input("number of position between 1-10: "))
while y_position > 10:
    y_position = int(input("number of position between 1-10: "))
game = Mastermind(x_color, y_position)
print(game)
Ans = game.answer()
guess_ = input("What is your guess?: ")
check_, rounds_ = game.check_num(Ans, guess_)
while check_ != ('*' * y_position):
    guess_ = input("What is your guess?: ")
    check_, rounds_ = game.check_num(Ans, guess_)
print(f"You solve it after {rounds_} rounds")
