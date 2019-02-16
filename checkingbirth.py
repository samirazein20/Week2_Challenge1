from datetime import datetime

# Prompting the user to enter their birth year
print('Enter Your Birth Year')

# Capturing the entered year from the keyboard
birthyear = int(input())

# getting the current year as an integer
thisyear = int(datetime.now().year)

# getting the persons age
diffyear = thisyear - birthyear

# checking 

if(diffyear < 18):
    print ("minor")
elif (diffyear > 36):
    print("elder")
else:
    print("youth")

