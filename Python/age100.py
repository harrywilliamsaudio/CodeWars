print("Please enter your name")
name = input()

print("Please enter your age")
age = int(input())

print("Hello", name, ".", "You are currently", age, "years old.")

from datetime import datetime

n = datetime.now()
t = n.timetuple()

currentYear, m, d, h, min, sec, wd, yd, i = t

centuryAge = (currentYear - age) + 100

print("You will turn 100 in", centuryAge, ".") 


