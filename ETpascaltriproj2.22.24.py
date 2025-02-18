# program that outputs a Pascal's Triangle based on the users input
# function for computing the binomial coefficient to calculate the Pascal Triangles

def pascaltriangle(n):
    for i in range(1, n+1):   #spacing for triangle
        for j in range(0, n-i+1):
            print(' ', end='')

    # the first element starts with 1 on each line
        c = 1
        for j in range(1, i+1):
            # first value is 1 on each line
            print(' ', c, sep='', end='')

            #calculate with the binomial coefficient
            c = c * (i - j) // j
        print()

# asking the user for a number of lines from 4-8, loop being used for invalid input
while True:
    try:
        n = int(input("Please enter a number between 4-8 for the number of lines in the Pascal Triangle: "))
        if n >= 1:
            break;
    except n<= 0:
        continue
n = pascaltriangle(n)
