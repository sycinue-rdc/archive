# Quadratic Formula Calculator
# Submitted by Dalumpines, Eunicys Sanchez
# BSCS-1 (Fundamentals to Programming) [10/16/2022]

### - - - Assignment For Lec #3 Discussion - - - ###

print("\nQuadratic Formula Calculator\n")

## - - Getting the inputs for A,B,C - - ##
a = float(input("Enter the value for A : "))
b = float(input("Enter the value for B : "))
c = float(input("Enter the value for C : "))

## - - Solving the Discriminant - - ##
d = (b*b)-(4*a*c)

print("\nDiscriminant Value =",d)

if d == 0 :
    print("\nThere is one real root.")

    x = -b/(2*a)
    print("X = ",x)

elif d > 0 :
    print("\nThere are two real roots.\n")

    ## - - Solving X1 & X2 - - ##
    x1 = (-b+d**(0.5))//(2*a)
    print("X1 =",x1)
    x2 = (-b-d**(0.5))//(2*a)
    print("X2 =",x2,"\n")

else :
    print("\nThere are two complex roots.\n")

    ## - - Solving X1 & X2 - - ##
    x1 = (-b+d**(0.5))/(2*a)
    print("X1 =",x1)
    x2 = (-b-d**(0.5))/(2*a)
    print("X2 =",x2,"\n")