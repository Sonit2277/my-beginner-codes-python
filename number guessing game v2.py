import random
secret = random.randint(1, 10)
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1
    
    if guess == secret:
        print("You got it in", attempts, "attempts!")
        break
    elif guess < secret:
        print("Too low, try again.")
    else:
        print("Too high, try again.")

if attempts == 5 and guess != secret:
    print("Game over! The number was", secret)