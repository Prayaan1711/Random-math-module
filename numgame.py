import random
playing = True

number = str(random.randint(10,20))

print("I will generate a number from 10 to 20 and you have to guess it")
print("The game ends when you gues right")

while playing:
    guess = input("Give me your best guess! ")
    if number == guess:
        print("You win!")
        print("The number was ", number)
        break

    else:
        print("You lose")