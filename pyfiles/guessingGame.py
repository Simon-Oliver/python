guess_count = 0
guess_limit = 3
secret_number = 9


while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    print(f'Nope! You have {guess_limit - guess_count} guesses remaining.')
    if guess == secret_number:
        print('You WIN!!!')
        break
else:
    print('Sorry you failed!')
