Score = int(input("Enter number:"))
def grade_calculator():
    if Score >= 90:
     print("Grade A")
    elif Score >= 80:
        print("Grade B")
    elif Score >= 70:
            print("Grade C")
    elif Score >= 60:
        print("Grade D")
    else:
            print("Grade E")
grade_calculator()