def poppython_start (question):
    while True:
        try:
            num = int(input(question))
            break
        except ValueError:
            print("You did not give me a number.")
            continue
    return num