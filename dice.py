import random
print("This is a dice simulation\n")
a = "y"

while a == "y":
    x=random.randint(1,6)
    if x==1:
        print("--------")
        print("|      |")
        print("|   0  |")
        print("|      |")
        print("--------")
    elif x==2:
        print("--------")
        print("|      |")
        print("|0    0|")
        print("|      |")
        print("--------")  
    elif x==3:
        print("--------")
        print("|   0  |")
        print("|0    0|")
        print("|      |")
        print("--------")
    elif x==4:
        print("--------")
        print("|0    0|")
        print("|0    0|")
        print("|      |")
        print("--------")  
    elif x==5:
        print("--------")
        print("|0    0|")
        print("|0    0|")
        print("|   0  |")
        print("--------") 
    elif x==6:
        print("--------")
        print("|0    0|")
        print("|0    0|")
        print("|0    0|")
        print("--------")

    b = input("Press y to roll again \n")