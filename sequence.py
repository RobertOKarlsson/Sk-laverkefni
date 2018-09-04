n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 0
num2 = 1
num3 = 0
summa = num1 + num2 + num3
for n in range(0,n):
    summa = num1 + num2 + num3
    num1 = num2
    num2 = num3
    num3 = summa
    print(summa)
    
