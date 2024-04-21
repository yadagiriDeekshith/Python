try:
    nume=int(input("Enter a number "))
    deno=int(input("Enter a number "))
    res=nume//deno
    print(res)
except ZeroDivisionError:
    print("Demominator error")
