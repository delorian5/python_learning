import random
def check_guess(guess, secret):
    if guess < secret:
        return "больше"
    elif guess > secret:
        return "меньше"
    else:
        return "угадал"
def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100, угадай")
    while True:
        guess = int(input("Твое число: "))
        attempts += 1
        results = check_guess(guess, secret)
        if results == "больше":
            print("Больше")
        elif results == "меньше":
            print("Меньше")
        else:
            print(f"Ты угадал с {attempts} попыток")
            break
play_game()