# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))#changed the '==' to '='  #add a bracket after int and corrected the single quote to double quotes

if year <= 1900: #added a colon after the condition
    print ("Woah, that's the past!") #changed the single quotes of the statement to be printed into double quotes
elif year > 1900 and year < 2020: #changed the && to and (logical operator)
    print ("That's totally the present!")
else: #changed elif to else due to syntax error
    print ("Far out, that's the future!!")
