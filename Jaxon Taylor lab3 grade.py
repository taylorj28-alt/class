#Jaxon Taylor
#10/8/2026
#introduction to python
#this code tell you what letter grade you got based on the score you put in to the terminal

def determine_grade(score):
    #Check if the score is within the valid range
    if score < 0 or score > 100:
        print("Error: The score must be between 0 and 100.")
        return None
    
    #Determine the corresponding letter grade
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


#Get input from the user before the function call

score = float(input("Enter your exam score (0-100): "))

grade = determine_grade(score)

print("Your letter grade is:", grade)