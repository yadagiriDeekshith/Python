def divide_by_3_count(number):
    count = 0
    while number > 10:
        number //= 3
        count += 1
    return count
number = int(input("Enter a number: "))
result = divide_by_3_count(number)
print(f"The number can be divided by 3 {result} times before it is less than or equal to 10.")
