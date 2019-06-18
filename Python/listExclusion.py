# List under than 10

a = [1, 1, 2, 3, 5, 8,9,9,9,9, 13, 21, 34, 55, 89]
limit = 10

for i in a:
    if a[i] < limit:
        print (a[i])
    else:
        print("Greater than ", limit)
        break
