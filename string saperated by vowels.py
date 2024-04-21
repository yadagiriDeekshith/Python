input_string=input("Enter a string to reverse it: ")
vowels="aeiouAEIOU"
for i in input_string:
    for i in vowels:
        input_string=input_string.replace(i," ")
    output=input_string.split()
dec=",".join(output)
print(dec)
