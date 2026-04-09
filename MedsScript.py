import os
import datetime

desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
file = os.path.join(desktopPath, "Meds.txt")

if not os.path.exists(file):
    print("Creating file...")
    day = str(input("What day of your medication are you on? "))

    # Get current date and time and assign them to variables
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%B %#d")
    time = now.strftime("%#I:%M %p")

    with open(file, "w") as f:
        f.write("Day ")
        f.write(day)
        f.write(" : ")
        f.write(date)
        f.write(" - ")
        f.write(time)
else:
    print("File exists")
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%B %#d")
    time = now.strftime("%#I:%M %p")

    with open(file, "r") as f:
        lines = f.readlines()

    lastLine = lines[-1]

    day = int(lastLine.split()[1])
    day += 1
    print("Printing day", day)

    with open(file, "a") as f:
        f.write("\nDay ")
        f.write(str(day))
        f.write(" : ")
        f.write(date)
        f.write(" - ")
        f.write(time)