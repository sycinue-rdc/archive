## - - BASIC CALCULATOR - - ##

device = input("What is your device? | PC / Mobile : ")
if device == "PC" :
    import os
    clear = lambda : os.system("cls")

if device == "Mobile" :
    import os
    clear = lambda : os.system("clear")

clear()

print("Basic Calculator\n")
print("Select the operation you wanted to use...\n")
operation = input("subtraction, addition, multiplication, division : ")

if operation == "subtraction" :
    clear()
    int1 = input("\nEnter the first value you want to subtract : ")
    sint1 = int(int1)
    int2 = input("Enter the value you want to subtract " + int1 + " to : ")
    sint2 = int(int2)
    sansw = sint1 - sint2
    fsub = str(sansw)
    print("\n" + int1 + " - " + int2 + " = " + fsub + "\n")
    print("The final answer is : " + fsub)
    exit()

if operation == "addition" :
    clear()
    int1 = input("\nEnter the first value you want to add : ")
    sint1 = int(int1)
    int2 = input("Enter the value you want to add  " + int1 + " to : ")
    sint2 = int(int2)
    sansw = sint1 + sint2
    fsub = str(sansw)
    print("\n" + int1 + " + " + int2 + " = " + fsub + "\n")
    print("The final answer is : " + fsub)
    exit()

if operation == "multiplication" :
    clear()
    int1 = input("\nEnter the first value you want to mutiply : ")
    sint1 = int(int1)
    int2 = input("Enter the value you want to multiplied " + int1 + " to : ")
    sint2 = int(int2)
    sansw = sint1 * sint2
    fsub = str(sansw)
    print("\n" + int1 + " x " + int2 + " = " + fsub + "\n")
    print("The final answer is : " + fsub)
    exit()

if operation == "division" :
    clear()
    int1 = input("\nEnter the first value you want to divide : ")
    sint1 = int(int1)
    int2 = input("Enter the value you want to divide " + int1 + " to : ")
    sint2 = int(int2)

    pause1 = input("Do you want to apply rounded off? y/n : ")
    if pause1 == "y" :
        sansw = sint1 // sint2
        fsub = str(sansw)
        print("\n" + int1 + " ÷ " + int2 + " = " + fsub + "\n")
        print("The final answer is : " + fsub)
        exit()
    if pause1 == "n" :
        sansw = sint1 / sint2
        fsub = str(sansw)
        print("\n" + int1 + " ÷ " + int2 + " = " + fsub + "\n")
        print("The final answer is : " + fsub)
        exit()

else :
    print("\nInvalid Operation, Please Try Again...")
    exit()