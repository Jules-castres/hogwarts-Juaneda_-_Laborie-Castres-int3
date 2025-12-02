def ask_text(message):
    while True:
        txt=input(message).strip
        if txt == '':
            return txt
        print("Invalide please try again")


def ask_choice(message,option):
    