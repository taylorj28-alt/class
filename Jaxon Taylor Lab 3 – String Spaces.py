#Jaxon Taylor
#10/8/2026
#introduction to python
#this code removes spaces from the phrase you put in to the terminal

def stripSpaces(myString):
    #Initialize an empty string to hold characters that are not spaces
    new_string = ""
    
    #Loop through the phrase character by character
    for char in myString:
        if char != " ":
            new_string += char  #Append the character if it's not a space
            
    return new_string


#Get input phrase from the user before the function call
user_phrase = input("Enter a phrase with spaces: ")

#Call the function to strip spaces
cleaned_phrase = stripSpaces(user_phrase)

#Print the new phrase to the screen
print(f"The phrase without spaces is: {cleaned_phrase}")
