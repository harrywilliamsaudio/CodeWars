# Valid Divisiors

print("Enter a number, and I will return the divisors")

number = int(input())

x = range(1, number)
divisors = []

for i in x:
    if (number % i == 0):
        divisors.append(i)

print("The valid divisors of", number, "are", divisors)
