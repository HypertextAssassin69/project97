import random
i = random.randint(1,9)
#print(i)
chance = 3

print("you have got ",chance," chances left, use them wisly")
userGuess = int(input("Please Enter Ur Guess: "))
while chance > 1 :
    chance -=1
    if userGuess>i:
        print("you have got ",chance," chances left, use them wisly")
        print("Ur Guess is Bigger Than The No. Please put a number smaller than ",userGuess)
        userGuess = int(input("Please Enter Another Guess: "))
    elif userGuess<i:
        print("you have got ",chance," chances left, use them wisly")
        print("Ur Guess is Smaller Than The No. Please put a number greater than ",userGuess)
        userGuess = int(input("Please Enter Another Guess: "))
if userGuess == i:
    print("WWWWOOOOWWWWW!!!! u guessed the number perfectly. u will be a great hacker someday.")
    chance = 2  

if  not chance > 1:
    print("you lose!!!!!!! and you won't become any sort of hacker in future. The Number Was ",i)
