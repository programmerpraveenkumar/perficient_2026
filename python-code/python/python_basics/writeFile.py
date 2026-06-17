# Ask user for input
user_input = input("Enter some text to save in file: ")
from datetime import datetime
current_datetime = datetime.now()
filename = str(current_datetime).replace(":","_")
# Open file in write mode and save input
with open(filename+".txt", "w") as file:
    file.write(user_input)

print("Your input has been saved to 'user_input.txt'")
