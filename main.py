import PIN
import PASS

print("Welcome to the Password/PIN generator!")

try:
    pin = input("Type 'PIN' if you want to generate a PIN. Otherwise the password generator will be opened: ")
    if pin == 'PIN' or pin == 'pin':
        PIN.pin_generator()

    else:
        PASS.password_generator()
except Exception as err:
    print("oops, something has gone wrong. Try it again" + str(err))
