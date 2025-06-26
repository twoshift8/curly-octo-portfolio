
cal = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def order():
    while True:
        try:
            date = input("Date: ").strip().title()
            if "/" in date:
                month, day, year = date.split("/")
                print(f"{int(year)}-{month:02}-{int(day):02}")

            elif "," in date:
                MMDD, YYYY= date.split(",")
                month, day = MMDD.split(" ")
                month = cal.index(month)+1
                print(f"{int(YYYY)}-{month:02}-{int(day):02}")
        except (ValueError, IndexError):
            pass
        except EOFError:
            break
        else:
            pass


if __name__ == "__main__":
    order()

#submit50 cs50/problems/2022/python/outdated
