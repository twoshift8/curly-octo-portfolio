#greeting = input("Press enter to walk up to the bank teller")

def main():
    #enter =
    input("Press any key to walk up to the bank teller.\n")
    greeting = input("You give the teller a friendly smile.\nWhat does the teller say in response?\nTeller: ").strip().lower()
    if greeting == "hello":
        print("You just made $0!")
    elif greeting[0] == "h":
        input("You say: \"I\'m gonna need to speak to a manager about compensation...\"\nPress any key to continue.")
        input("\n10 minutes later:\nManager:\"Hows $20 sound?\"\nPress any key to accept.")
        print("You just made $20!")
    else: #greeting[0:] != "h":
        print("You just made $100!")

main()


#check50 cs50/problems/2022/python/bank
