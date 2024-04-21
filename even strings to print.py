input_string=input("Enter a string to reverse it: ")
words=input_string.split()
even_length=[]
for i in words:
    if len(i)%2==0:
        even_length.append(i)
output_string=" ".join(even_length)
print(output_string)
