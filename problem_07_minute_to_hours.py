mins = int(input("Enter the number of minutes you'd like to convert to hours and minutes: "))
hours = mins//60
new_mins = mins % 60

print(str(mins) + " minutes is " + str(hours) + " hours and " + str(new_mins) + " mins")
