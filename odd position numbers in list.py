def display_elements_at_odd_indexes(input_list):
    for i in range(1, len(input_list), 2):
        print(input_list[i])
input_list = input("Enter a list of elements separated by spaces: ").split()
input_list = [int(x) for x in input_list]

if len(input_list) < 2:
    print("Please enter at least two elements in the list.")
else:
    print("Elements at odd index positions:")
    display_elements_at_odd_indexes(input_list)

