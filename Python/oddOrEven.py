print("Please enter a number, I will tell you if it's Odd or Even")
number = int(input())
    
while number != 0:
    
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

    print("Again")
    number = int(input())
