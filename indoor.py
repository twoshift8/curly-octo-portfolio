def quiet(who="mr. patrick star"):
    greet = input("Welcome to the I-brary!\nType your name, but please keep your voice down. ").lower()
    if not greet:
        return who
    return greet

def silence():
        print("KEEP YOUR VOICE DOWN,", quiet(), "! \nACTUALLY, GET OUT!!")


silence()
