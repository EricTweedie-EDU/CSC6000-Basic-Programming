import math
# Asking the user for a number to assign how many subsets
j = int(input("Choose a number between 3-8 for your subsets: "))

# function to get the sum of the sizes after gathering the input from j
def subset_sum(total):
    """finding the sum of subset sizes"""
    theSum = 0
    for i in total:
        theSum = theSum + i
    return theSum

# using the input from j to assign the size of each subset

if j == 3:
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    subsets_all = m1,m2,m3
    subset_sum(subsets_all)
    
    
elif j == 4:
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    m4 = int(input("Enter the size of your 4th subset, use #1-5: "))
    subsets_all = m1,m2,m3,m4
    subset_sum(subsets_all)
    
    
elif j == 5:
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    m4 = int(input("Enter the size of your 4th subset, use #1-5: "))
    m5 = int(input("Enter the size of your 5th subset, use #1-5: "))
    subsets_all = m1,m2,m3,m4,m5
    subset_sum(subsets_all)
    
    
elif j == 6:
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    m4 = int(input("Enter the size of your 4th subset, use #1-5: "))
    m5 = int(input("Enter the size of your 5th subset, use #1-5: "))
    m6 = int(input("Enter the size of your 6th subset, use #1-5: "))
    subsets_all = m1,m2,m3,m4,m5,m6
    subset_sum(subsets_all)
    
    
elif j == 7:
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    m4 = int(input("Enter the size of your 4th subset, use #1-5: "))
    m5 = int(input("Enter the size of your 5th subset, use #1-5: "))
    m6 = int(input("Enter the size of your 6th subset, use #1-5: "))
    m7 = int(input("Enter the size of your 7th subset, use #1-5: "))
    subsets_all= m1,m2,m3,m4,m5,m6,m7
    subset_sum(subsets_all)
    
    
else:
    j == 8
    print("You entered {number} subsets, enter the size of each one now.".format(number=j))
    m1 = int(input("Enter the size of your 1st subset, use #1-5: "))
    m2 = int(input("Enter the size of your 2nd subset, use #1-5: "))
    m3 = int(input("Enter the size of your 3rd subset, use #1-5: "))
    m4 = int(input("Enter the size of your 4th subset, use #1-5: "))
    m5 = int(input("Enter the size of your 5th subset, use #1-5: "))
    m6 = int(input("Enter the size of your 6th subset, use #1-5: "))
    m7 = int(input("Enter the size of your 7th subset, use #1-5: "))
    m8 = int(input("Enter the size of your 8th subset, use #1-5: "))
    subsets_all=m1,m2,m3,m4,m5,m6,m7,m8
    subset_sum(subsets_all)
    
# asking the user for the total number of the arrangement
# the number is smaller than the sum of the sizes of the subsets
k = int(input("Enter the total number of the arrangement, a # smaller than {snumber}: ".format(snumber=subset_sum(subsets_all))))
n = subset_sum(subsets_all)
subset_list = list(subsets_all) #changing subsets_all from tuple to list

# variable to save the value of n-k and get the factorial of the number
combo_fact = math.factorial((n-k))

# finding the factorial of a given number 
def factorial(n):
    """calculating the factorials of a given number"""
    fact = 1
    for factor in range(1, n+1):
        fact *= factor
    return fact

fact_list = [factorial(x) for x in subset_list]

#function to multiply the factorial list together into 1 number
def multiply_list(fact_list):
    """taking the numbers from a list and calculating the factorials"""
    product = 1
    for x in fact_list:
        product *= x
    return product
total_fact = multiply_list(fact_list)

arrangements = math.factorial(n)/(combo_fact*total_fact)
print("Given your inputs, the number of arrangements is: ", arrangements)
