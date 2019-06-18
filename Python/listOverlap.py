# List comparison

a = [1, 1, 2,2,2,2,2,2,2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4,5,5,5,5,5,5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []

for element in b:
    if element in a and element not in common:
            common.append(element)

print(common)
        
