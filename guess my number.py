low = 0 
high = 100

guess = (low - high) // 2

while True:
    print(f'Is your secret number {guess}?')
    ask = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if ask == "c":
        break
    elif ask == "h":
        high = guess
    elif ask == "l":
        low = guess
    else :
        print("Sorry, I did not understand your input.")
        continue
    guess = (low - high) // 2 
print(f"Game over. Your secret number was:{guess}")