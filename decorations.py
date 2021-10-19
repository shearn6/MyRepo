def get_num(question):
    def decorator(func):
        def wrapper():
            while True:
                try:
                    num = int(input(question))
                    return func(num)
                except ValueError:
                    print("You don't do numbers often, do you? ")
        return wrapper
    return decorator

@get_num("Give me a positive number: ")
def get_pos(num):
    if num > 0:
        return num
    else:
        print("That is not a positive number.")
        return get_pos()

@get_num("Give me an even number: ")
@get_pos
def get_even(num):
    mmod = num % 2
    if mod == 1:
        return num
    else:
        print("Your number is not even")
        return get_even()

if __name__ == '__main__':
    def main():
        num = get_even()
        print(f"Your number is {num}.")

    main()
