print("Reverse Text using functions \nby: Clyde Joshua C. Belongilot")
print("----------------------------")

while True:
    text = input("Enter text:")

    if text.isdigit():
        print("Invalid Operation! Use text only.")
        print("---------------------------------")


    else:
        reverse = text[::-1]
        print("Result:", reverse); print()

        choice = input("Do you want to print more text(Y/N)?")
        if choice.lower() == 'n':
            print("Thank you!")
            break


