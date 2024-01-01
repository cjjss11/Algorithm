num1 = int(input())
num2 = int(input())
three = num1 * (num2 % 10)
num2 = num2 // 10
four = num1 * (num2 % 10)
num2 = num2 //10
five = num1 * (num2 % 10)
six = three + four * 10 + five * 100
print(three)
print(four)
print(five)
print(six)