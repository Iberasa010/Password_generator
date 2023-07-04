import secrets


def password_generator():
    # Password generator. After a brief introduction and if "PIN" or "pin" has not been typed
    # in the main function this code will be displayed.
    # A number of passwords to be given and the length of those passwords will be asked,
    # Then a random password will be generated with the secrets() class.
    # If the advanced version is executed the user will be able to customize the password.
    # Otherwise only the length and the number of password will be selected.
    try:
        secret_pass = secrets.SystemRandom()
        print("")
        print("Welcome to the password generator! You can either take the basic plan to get passwords containing\n"
              "lower-case, upper-case, special characters and numbers or get the advanced plan where you can\n"
              "customize your password and what type of characters it has! ")
        print("")
        basic = input("Do you want to use the basic plan? Type 'No' if not: ")

        if basic != 'no' and basic != 'No':

            possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"$%/()=¡!-\':;,.1234567890'

            num_pass = int(input("How many passwords do you want to generate? "))

            len_pass = int(input("How long do you want these passwords to be? "))
            print("")

            print("Generated passwords: ")
            for numpass in range(num_pass):
                passw = ''
                for lenpass in range(len_pass):
                    passw = passw + secret_pass.choice(possible_chars)
                print(passw)

            print("")
            print("Remember, you can always select shorter or longer passwords if needed! You can also "
                  "check the advanced version or try the PIN feature")

        else:
            # If the advanced plan is requiered then this code will be displayed. The user will be able
            # to choose which characters he wants on his password.
            num_pass = int(input("How many passwords do you want to generate? "))

            len_pass = int(input("How long do you want these passwords to be? "))

            mayus = input("Do you want to use MAYUS characters? type 'No' if not: ")
            numbers = input("Do you want to use numbers? type 'No' if not: ")
            special = input("Do you want to use special characters? type 'No' if not: ")

            if mayus == 'No' or mayus == 'no':
                if numbers == 'No' or numbers == 'no':
                    if special == 'No' or special == 'no':
                        chars = 'abcdefghijklmnopqrstuvwxyz'
                    else:
                        chars = 'abcdefghijklmnopqrstuvwxyz!"$%/()=¡!-\':;,.'
                else:
                    if special == 'No' or special == 'no':
                        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
                    else:
                        chars = 'abcdefghijklmnopqrstuvwxyz1234567890!"$%/()=¡!-\':;,.'
            else:
                if numbers == 'No' or numbers == 'no':
                    if special == 'No' or special == 'no':
                        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    else:
                        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"$%/()=¡!-\':;,.'
                else:
                    if special == 'No' or special == 'no':
                        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                    else:
                        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"$%/()=¡!-\':;,.'

            print("Generated passwords: ")
            for numpass in range(num_pass):
                passw = ''
                for lenpass in range(len_pass):
                    passw = passw + secret_pass.choice(chars)
                print(passw)

            print("")
            print("Remember, you can always select shorter or longer passwords if needed! You can also "
                  "check the simple version or try the PIN feature! ")

    except Exception as err:
        print("Oops. Something unexpected has happened and the following error has occured: " + str(err) +
              ". Try again")
