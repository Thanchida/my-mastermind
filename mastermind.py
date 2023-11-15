import random


class Guess:
    def __init__(self, x=1, y=1):
        self.colors = x
        self.positions = y
        self.num = []

    def set_colors(self,colors):
        self.colors = colors

    def get_colors(self):
        return self.colors

    def set_positions(self,positions):
        self.positions = positions

    def get_positions(self):
        return self.positions

    def start(self):
        print(f'Playing Mastermind with {self.colors} colors and {self.positions} positions')

    def num_guess(self):
        self.num = []
        self.num.clear()
        g = input('What is your guess?: ')
        for n in g:
            self.num.append(n)
        print(f'Your guess is {g}')
        return self.num


class Answer:
    def __init__(self, guess):
        self.guess = guess

    def set_guess(self, guess):
        self.guess = guess

    def get_guess(self):
        return self.guess

    def check_num(self, correct):
        for i in range(len(self.guess)):
            if int(self.guess[i]) == correct[i]:
                print('*', end='')
            elif int(self.guess[i]) in correct:
                print('o', end='')
            else:
                print('', end='')


color = int(input('How many color?: '))
position = int(input('How many position?: '))
game = Guess(color,position)
game.start()
guess = game.num_guess()
answer = Answer(guess)
correct = random.sample(range(1, 8), position)
print(correct)
n = 0
while True:
    answer.check_num(correct)
    n += 1
    int_guess = [int(x) for x in guess]
    if int_guess == correct:
        print()
        print(f'You solve it in {n} rounds')
        break
    print()
    guess = game.num_guess()
    answer.set_guess(guess)


