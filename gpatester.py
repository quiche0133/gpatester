# Adithya Senthil
# gpatester.py
# intakes a student's full name and gpa, and returns what honors status they have received

lastname = "PLACEHOLDER"
firstname = "PLACEHOLDER"
gpa = 0.0
print("Enter 'ZZZ' for last name to quit.")
while lastname != "ZZZ":
    lastname = input("Enter last name: ")
    if lastname == "ZZZ":
        break
    firstname = input("Enter first name: ")
    gpa = float(input("Enter GPA: "))
    if gpa >= 3.5:
        print(firstname + " " + lastname + " has made the Dean's List!")
    elif gpa >= 3.25:
        print(firstname + " " + lastname + " has made the Honor Roll!")
    else:
        print(firstname + " " + lastname + " has not qualified for the Dean's List or the Honor Roll.")