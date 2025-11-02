import numpy as np

number = np.random.randint(1, 100)
count = 0

while True:
    count += 1
    predicted_number = int(input("Guess the number: "))
    if predicted_number > number:
        print("The guessed number is less")
    elif predicted_number < number:
        print("The guessed number is more")
    else:
        print(f"That's right! You've guessed the number {number} in {count} attempts")
        break