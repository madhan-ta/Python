series = int(input("enter the series to be printed:"))
#series = 10
print("printing series for ", series)
j = series
while j >= 1:
    for i in range(1, j):
        print(i, end=' ')
        i = i + 1
    print()
    j = j - 1





