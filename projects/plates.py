
'''
vanity plates must:
    1 - start with at least two letters.”
    2 - contain a min of 2 and max of 6 characters
        (letters or numbers)
    3 - Numbers cannot be used in the middle of a plate;
        they must come at the end.
    4 - First number used cannot be a ‘0’.”
    5 - No periods, spaces, or punctuation marks are allowed.
'''

def main():
    plate = input("Plate: ").strip()
    while is_valid(plate):
        print("Valid")
        break
    else:
        print("Invalid")

def is_valid(s):

    if not s.isalnum(): #5
        return False
    if not s[0:2].isalpha(): #1
        return False
    if not 2 <= len(s) <= 6: #2
        return False

    n1 = False #flag indicating "first digit has been found"

    for i in range(len(s)):
        if not s[i].isalpha(): # checks if this character is a digit
            n1 = True # marks that weve seen a digit
            if s[i] == "0": # checks if its 0
                return False
        elif n1 and s[i].isalpha(): # after seeing a number do we see a letter? bc no bueno
            return False

    return True

if __name__ == "__main__":
    main()

#submit50 cs50/problems/2022/python/plates
