def collatz(number):
    is_even = False
    is_even = (number % 2) == 0

    if is_even:
        print(number // 2)
        return number // 2
    else:
        print( 3 * number + 1 )
        return 3 * number + 1
    
try:
    number = int(input("Please input the number="))

    while number != 1:
        number = collatz(number)
except ValueError:
    print("You should provide valid integer number")

