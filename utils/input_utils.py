def ask_number(message, min_val=None, max_val=None):
    """
    :param message: The function ask a number and verify if it is a real number
                    between min_val and max_val with the potential case of negative numbers then return it if valid.
    :param min_val: int
    :param max_val: int
    :return: int
    """
    valid_number = False
    number = 0

    while not valid_number:
        c = input(message).strip()

        if len(c) == 0:
            print("Please enter a valid number.")
        else:
            # It verifies if the number is valid or not
            start = 0
            negative = False

            # Gestion of the negative sign
            if c[0] == '-':
                if len(c) == 1:  # if it's just a "-"
                    print("Please enter a valid number.")
                else:
                    negative = True
                    start = 1
                    is_valid = True

                    # Verify if all characters are digits
                    i = start
                    while i < len(c) and is_valid:
                        if ord(c[i]) < ord('0') or ord(c[i]) > ord('9'):
                            is_valid = False
                        i = i + 1

                    if not is_valid:
                        print("Please enter a valid number.")
                    else:
                        # Convert text in numbers
                        number = 0
                        for j in range(start, len(c)):
                            digit = ord(c[j]) - ord('0')
                            number = number * 10 + digit

                        number = -number

                        # Vérify that the number is between min_val and max_val
                        if min_val is not None and number < min_val:
                            if max_val is not None:
                                print(f"Please enter a number between {min_val} and {max_val}.")
                            else:
                                print(f"Please enter a number greater or equal to {min_val}.")
                        else:
                            if max_val is not None and number > max_val:
                                if min_val is not None:
                                    print(f"Please enter a number between {min_val} and {max_val}.")
                                else:
                                    print(f"Please enter a number lower or equal to {max_val}.")
                            else:
                                valid_number = True
            else:
                # No negative sign
                is_valid = True

                # Verify if each character is digit
                i = 0
                while i < len(c) and is_valid:
                    if ord(c[i]) < ord('0') or ord(c[i]) > ord('9'):
                        is_valid = False
                    i = i + 1

                if not is_valid:
                    print("Please enter a valid number.")
                else:
                    # Convert text into numbers
                    number = 0
                    for j in range(len(c)):
                        digit = ord(c[j]) - ord('0')
                        number = number * 10 + digit

                    # Vérify that the number is between min_val and max_val
                    if min_val is not None and number < min_val:
                        if max_val is not None:
                            print(f"Please enter a number between {min_val} and {max_val}.")
                        else:
                            print(f"Please enter a number greater or equal to {min_val}.")
                    else:
                        if max_val is not None and number > max_val:
                            if min_val is not None:
                                print(f"Please enter a number between {min_val} and {max_val}.")
                            else:
                                print(f"Please enter a number lower or equal to {max_val}.")
                        else:
                            valid_number = True

    return number

def ask_text(message):
    while True:
        txt=input(message).strip
        if txt == '':
            return txt
        print("Invalide please try again")

def ask_choice(message,option):
    return 0
