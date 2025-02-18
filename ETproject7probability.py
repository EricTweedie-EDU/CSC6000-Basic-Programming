#The Lottery winning numbers game

#Asking the user for the total number of numbers in the game

n = int(input("Please provide a value for the total number of numbers in the Lottery Game: "))

#Asking the use for the number of numbers needed to win the jackpot

k = int(input("What is the correct number of numbers needed to win the jackpot: "))

# function to calculate all the possible arrangements of the total numbers
def combination(k,n):
    ans = 1
    for i in range(n, n-k, -1):
        ans *= i
    for i in range(2, k+1):
        ans /= i
    return round(ans)

# placing combinations as denominator since there is only 1 favorable outcome
probability = f"1 / {str(combination(k,n))}"

print(f"Your chances of winning the jackpot are: {probability}!")

# user still wins if they match k-1 numbers in the game, total combinations are still the same

winner = f"{str(k)} * {str(n - k)} / {str(combination(k,n))}"

minus_k = (k - 1)
print(f"You still win if you match {minus_k} but your chances are: {winner}!")
