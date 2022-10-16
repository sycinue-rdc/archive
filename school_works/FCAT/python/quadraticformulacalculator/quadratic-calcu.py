# Basic Quadratic Formula Calculator
# Self Study Proj. #4
# Copyright (c) Dalumpines, Eunicys S.
# Revised Copy [Submitted to Prof. Manny Bernabe]
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


### - - -  IGNORE THE FOLLOWING LINES - - - ###
## - - Self Study Proj. Experimental #4 - - ##
#
#sim1 = -4 * a *c
#sim2 = b ** 2
#sim3 = -1 * b
#sim4 = 2 * a
#
#if sim1 > 0 :
#    sol1 = sim1 + sim2
#    sol2 = sol1 ** 0.5
#
#    s1x1 = sim3 + sol2
#    s2x1 = s1x1 / sim4
#
#    s1x2 = sim3 - sol2
#    s2x2 = s1x2 / sim4
#
#    print("\nx1 = " + str(s2x1))
#    print("x2 = " + str(s2x2))
#
#else :
#    sol1 = sim1 - sim2
#    sol2 = sol1 ** 0.5
#
#    s1x1 = sim3 + sol2
#    s2x1 = s1x1 / sim4
#
#    s1x2 = sim3 - sol2
#    s2x2 = s1x2 / sim4
#
#    print("\nx1 = " + str(s2x1))
#    print("x2 = " + str(s2x2))