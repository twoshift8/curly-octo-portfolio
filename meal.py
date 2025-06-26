
'''
breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00,
dinner between 18:00 and 19:00
'''

time = input("time?\n[#:## or ##:## format]\n").strip()
# In an improved version,
# I would add input validation to remove letters or invalid characters,
# but we haven't learned those tools yet.
def main():
    clock = convert(time)
    if 7<= clock <=8 :
        return print("breakfast time")
    elif 12<= clock <=13 :
        return print("lunch time")
    elif 18<= clock <=19 :
        return print("dinner time")
    #else: return print("not time to eat")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours + minutes

if __name__ == "__main__":
    main()


'''
__name__ is like an invisible header that Python sets for you automatically.
When you run the file directly (like python meal.py), Python adds an invisible header that says:
    __name__ = "__main__"

When you import the file into another script (like import meal), Python changes the invisible header:
__name__ = "meal"
'''

#check50 cs50/problems/2022/python/meal
