#Jaxon Taylor
#10/8/2026
#introduction to python


def determine_grade(score):
    # Check if the score is within the valid range
    if score < 0 or score > 100:
        print("Error: The score must be between 0 and 100.")
        return None
    
    # Determine the corresponding letter grade
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

# Main program block
# 1. Get input from the user before the function call
try:
    user_score = float(input("Enter the exam score (0-100): "))
    
    # 2. Call the function
    letter_grade = determine_grade(user_score)
    
    # 3. Print the result if a valid grade was returned
    if letter_grade is not None:
        print(f"The corresponding letter grade is: {letter_grade}")
        
except ValueError:
    print("Error: Please enter a valid numerical score.")
