import random

good = "Warm!"

bad = "Cold!"

round_num = 1

num = random.randint(0, 100)

print(num)

print('Guessing Game Challenge!')
print('')
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're: Cold!")
print("If your guess is within 10 of my number, I'll tell you you're: Warm!")
print("Let's play!")

print('')

print("Number of round: {}".format(round_num))
guess = int(input("I'm thinking of a number between 1 and 100.\nWhat is your guess? "))

while guess < 0 or 100 < guess:
    guess = int(input("I'm thinking of a number between 1 and 100.\nWhat is your guess? "))

while guess != num:
    if -10 < guess - num < 10:
        print('\n' + good)
        answer = good
    else:
        print('\n' + bad)
        answer = bad
    round_num += 1
    print("\nNumber of round: {}".format(round_num))
    guess = int(input("I'm thinking of a number between 1 and 100.\nWhat is your guess? "))
else:
    if round_num == 1:
        print('\nCongratulations! You win the game in {} round! The guessing number was: {}'.format(round_num, num))
    else:
        print('\nCongratulations! You win the game in {} rounds! The guessing number was: {}'.format(round_num, num))