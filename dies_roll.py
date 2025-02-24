import random

def next_game():
    n_choice = input('Do you want to play again? (y/n) ').strip().lower()
    return n_choice == 'y'

print("Welcome to the Die Roll Game!")

while True:
    choice = input('Roll the die? (y/n): ').strip().lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled: {die1}, {die2}')

        if not next_game():
            print('Okay, Have a good time!')
            break
    elif choice == 'n':
        print('Thanks for playing!')
        break  # Exit loop
    else:
        print('Please insert a valid choice (y/n)!')
