age = int(input("Enter the age:"))
weight = int(input("Enter the weight:"))
def medicine_program():
    if age < 18 and weight < 55:
        print("you are not eligible for it.")
    elif weight >= 55 and age >=18:
        print("This medicine is for you.")
    else:
        print("Medicine cannot be administered. Patient is under 15.")
medicine_program()