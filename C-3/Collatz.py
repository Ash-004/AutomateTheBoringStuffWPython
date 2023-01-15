def collatz(number):
    if not number%2:
        number = number // 2
        return number
    else:
        number = (3 * number) + 1
        return number

try:
    n = int(input("Number: "))
except ValueError:
    print("Only numbers dood")

try:
    while n != 1:
        n=collatz(n)
        print(n)
except NameError:
    print("You got some ERRORSSS")
    