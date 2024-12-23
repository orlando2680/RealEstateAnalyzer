strName = input("Enter the person's name for whom the Grade Analyzer is: ")
try:
    intScore1 = int(input("Enter Test Score 1: "))
    intScore2 = int(input("Enter Test Score 2: "))
    intScore3 = int(input("Enter Test Score 3: "))
    intScore4 = int(input("Enter Test Score 4: "))
except ValueError:
    print("Please enter valid whole numbers for test scores.")
    exit()
if intScore1 < 0 or intScore2 < 0 or intScore3 < 0 or intScore4 < 0:
    print("Test scores must be greater than 0.")
    exit()
strDropLowest = input("Should the lowest grade be dropped from the calculation? (Y/N): ").upper()
if strDropLowest not in ["Y", "N"]:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()
if strDropLowest == "Y":
    if intScore1 <= intScore2 and intScore1 <= intScore3 and intScore1 <= intScore4:
        fltAverage = (intScore2 + intScore3 + intScore4) / 3.0
    elif intScore2 <= intScore1 and intScore2 <= intScore3 and intScore2 <= intScore4:
        fltAverage = (intScore1 + intScore3 + intScore4) / 3.0
    elif intScore3 <= intScore1 and intScore3 <= intScore2 and intScore3 <= intScore4:
        fltAverage = (intScore1 + intScore2 + intScore4) / 3.0
    else:
        fltAverage = (intScore1 + intScore2 + intScore3) / 3.0
else:
    fltAverage = (intScore1 + intScore2 + intScore3 + intScore4) / 4.0
fltAverage = float(fltAverage)
if fltAverage >= 97.0:
    strGrade = "A+"
elif fltAverage >= 94.0:
    strGrade = "A"
elif fltAverage >= 90.0:
    strGrade = "A-"
elif fltAverage >= 87.0:
    strGrade = "B+"
elif fltAverage >= 84.0:
    strGrade = "B"
elif fltAverage >= 80.0:
    strGrade = "B-"
elif fltAverage >= 77.0:
    strGrade = "C+"
elif fltAverage >= 74.0:
    strGrade = "C"
elif fltAverage >= 70.0:
    strGrade = "C-"
elif fltAverage >= 67.0:
    strGrade = "D+"
elif fltAverage >= 64.0:
    strGrade = "D"
elif fltAverage >= 60.0:
    strGrade = "D-"
else:
    strGrade = "F"
print(f"\nGrade Analyzer Results for {strName}:")
print(f"Average Score: {fltAverage:.1f}")
print(f"Letter Grade: {strGrade}")