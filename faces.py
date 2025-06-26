
s = input("Hows your day been? (feel free to use smiley or frowny faces.) \n")

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    s = s.replace(":I", "😐")
    return s

def main():
    convert(s)
    print("\nyou said:\n", f"{convert(s)}", "\nbeep, boop... \n...\ndont care. \nbye, have a beautiful time.")

main()
