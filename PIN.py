import secrets


def pin_generator():
    # PIN generator. After a brief introduction and if "PIN" or "pin" has been typed
    # in the main function, every time "PIN" or "pin" is typed in console
    # a number of PINS to be given will be asked.
    # Then a random number will be generated with the secret() class.
    # NOTE: It would be easier to generate a number between 1000 and 9999, but I wanted
    # to practice with the secret's functions, max efficiency is not the focus of this code.
    secret_pin = secrets.SystemRandom()
    rolling = True
    while rolling:
        pin = input("Welcome to the PIN generator! Generate a new PIN typing 'PIN' in"
                    " the console. Write 'EXIT' to leave the PIN generator: ")
        if pin == 'PIN' or pin == 'pin':
            num_pins = int(input("How many PINS do you want?: "))
            for pins in range(num_pins):
                psw = ''
                for pin in range(4):
                    psw = psw + str(secret_pin.randint(0, 9))
                print(psw)
            print("These are the generated PINS. Remember to keep them secret!")
        elif pin == 'EXIT' or pin == 'exit':
            print("See you later! Don't forget to check the password generator!")
            rolling = False
        else:
            print("Remember to write PIN to get a new PIN or EXIT to leave :D")
