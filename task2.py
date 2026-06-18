#Task 2

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

add = lambda *args: sum(args)

multiply = lambda *args: (
    1 if len(args) == 0
    else args[0] * multiply(*args[1:])
)

user_input = input("Enter Operation add/multiply/factorial: ").lower()

if user_input == "add":
    nums = tuple(map(int, input("Enter numbers seperated by space: ").split()))
    print(add(*nums))

elif user_input == "multiply":
    nums = tuple(map(int, input("Enter numbers seperated by space: ").split()))
    print(multiply(*nums))

elif user_input == "factorial":
    n = int(input("Enter the number you want to find the factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Result:", factorial(n))
else:
    print("Invalid User_input")