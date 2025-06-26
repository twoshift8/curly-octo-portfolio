
guess = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n").strip().lower()

def main():
    match guess:
        case "42"|"forty-two"|"forty two"|"fortytwo":
            print("Yes")
        case "69"|"420":
            print("No, but good guess!")
        case _:
            print("No")

main()


'''
def other():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n").strip().lower()
    if ans == "42" or ans == "forty-two" or ans == "forty two" or ans == "fortytwo":
        print("Yes")
    if ans == "69" or ans == "420":
        print("No, but good guess!")
    else:
        print("No")

other()
'''

#check50 cs50/problems/2022/python/deep
