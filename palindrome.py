number=int(input("Enter a number to find palindrome "))
reverse_number=0
orginal_number=number
while number > 0:
    temp=number%10
    reverse_number=reverse_number*10+temp
    number//=10
if orginal_number==reverse_number:
    print("Palindrome")
else:
    print("Not a palindrome")
