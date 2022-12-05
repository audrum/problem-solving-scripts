num = 0
result = 0
while num <= 100:
    if (num % 3 == 0) or (num % 5 == 0):
        print(num)
    result += num
    num += 1
print(f"The sum of all multiples is {result}")
