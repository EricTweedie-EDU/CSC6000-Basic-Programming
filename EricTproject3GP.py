# program that is asking the user for a scale factor (A) and a common ratio (R), to create a GP.
import math

a = float(input("Please enter a number for a scale factor: "))
r = float(input("Please enter a number for a common ratio: "))

# using the input from the user, inform them if the GP converges, what the sum is, and the first 3 elements

if (r < 1)and (r > -1):
    infinsum = a/(1 - r)
    print("This GP converges with infinite elements to ", infinsum)
    a1 = a
    a2 = a*r
    a3 = a*r**2
    print("The first 3 elements are: ",a1,a2,a3)

else:
    r >= 1 or r >= -1
    n = float(input("This GP does not converge to a finite number, how many elements are there?: "))
    finitesum = a*(r**n - 1)/(r - 1)
    print("The GP sum with ", n, "elements is equal to ", finitesum)
    n1 = a
    n2 = a*r
    n3 = a*r**2
    print("The first 3 elements are: ",n1,n2,n3)

