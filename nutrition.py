
name = input("Item: ").strip().lower().replace(" ", "")
fruits = {
    "apple": 130,
    "avocado california": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


#if/call version

def fruit(name):
    if name in fruits:
        print("Calories: "+f"{fruits[name]}")
    return

'''
# loop version
def fruit(name):
    for fruit in fruits:
        if fruit == name:
            print("Calories: "+f"{fruits[fruit]}")
            break
'''

if __name__ == "__main__":
    fruit(name)

#submit50 cs50/problems/2022/python/nutrition
