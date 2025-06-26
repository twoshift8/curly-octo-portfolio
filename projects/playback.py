def main():
    hello = input("Hi... I'm... Sam... the... Sloth... \nWhat's... your... name..? \n").title()
    print(f"Hi.., {hello}...")
    day = input("How's... your... day... been..? \n")
    reverb = day.replace(' ', '...')
    print("Oh... did.. you.. say..:", reverb, "? \n Just... Take... a... Nap...\n")

main()
