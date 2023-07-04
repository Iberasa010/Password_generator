import random


def pin_generator():
    rolling = True
    while rolling:
        pin = input("Welcome to the PIN generator! Generate a new PIN typing 'PIN' in"
                    " the console. Write 'EXIT' to leave the PIN generator: ")
        if pin == 'PIN' or pin == 'pin':
            num_pins = int(input("How many PINS do you want?: "))
            for pins in range(num_pins):
                psw = ''
                for pin in range(4):
                    psw = psw + str(random.randint(0, 9))
                print(psw)
            print("These are the generated PINS. Remember to keep them secret!")
        elif pin == 'EXIT' or pin == 'exit':
            print("See you later! Don't forget to check the password generator!")
            rolling = False
        else:
            print("Remember to write PIN to get a new PIN or EXIT to leave :D")
