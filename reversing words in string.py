input_string=input("Enter a string to reverse it: ")
words=input_string.split()
reverse_words=words[::-1]
output_string=" ".join(reverse_words)
print(output_string)
