def vote(citizen, age, residency, registration):
    if citizen == "y" and age == "y" and residency == "y" and registration == "y":
        print("Congratulations! You are eligible to vote.")
    elif citizen != "y" or citizen != "Y" or age != "y" or age != "Y" or residency != "y" or residency != "Y" or registration != "y" or registration != "Y": 
        print("You are ineligible to vote")
    else:
        print("error")

citizenship = input("Are you a U.S. citizen? (Type y or n for yes or no)  ")
age_requirement = input("Are you at least 18 years old? (Type y or n for yes or no)  ")
resident = input("Do you reside in the U.S? (Type y or n for yes or no)  ")
register = input("Have you registered to vote? (Type y or n for yes or no)  ")

vote(citizenship, age_requirement, resident, register)
