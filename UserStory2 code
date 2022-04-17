#UserStory2: As the instructor, want to see classes booking info to send follow-up info/reminders:
## need db info for this

#see booking informations from form.
#needs database before we can start to create functional code
# so this is basic skeleton outline


print("==========================================")
print("         ~ Booking Information Record ~")
print("==========================================")
print("Available Options:")
print("A) Add Record\t\tB) View Record")
print("C) Clear Records\tD) Exit Website\n")
print()
selection = str(input("Select an option [A,B,C,D]: "))

try:
    file = open("record.txt", "r")
except FileNotFoundError:
    file = open("record.txt", "x")

if selection.upper() == "A":
    var1 = str(input("Enter Name: "))
    var2 = str(input("Enter Email: "))
    var3 = str(input("Enter Address: "))
    file = open("record.txt", "a")
    file.write(f"\n{var1}, {var2}, {var3}")
    file.close()
elif selection.upper() == "B":
    file = open("record.txt", "r")
    print(file.read())
    file.close()
elif selection.upper() == "C":
    print("No records found.")
    file = open("record.txt", "r+")
    file.truncate(0)
    file.close()
elif selection.upper() == "D":
    print("Thank you")
else:
    print("Option not recognised, please try again.")

#works 
