#Collect user name and welcome the user

print("Welcome to the Eco Quiz!")
name = input("Enter your name:")
print (" Hello " + name)

#Define Questions about the issue/plastic poloution and state common plastic items

# the questions with the most plastic items that will be asked until all answers are given but only from the yes or no

questions = [
    "Did you use a plastic water bottle today? (yes/no): ",
    "Did you use a plastic bag today? (yes/no): ",
    "Did you use any plastic food wrappers today? (yes/no): ",
    "Did you use plastic cutlery today? (yes/no): ",
    "Did you drink from a plastic straw today? (yes/no): "
]


items = [
    "plastic water bottle",
    "plastic bag",
    "plastic food wrappers",
    "plastic cutlery",
    "plastic straw"
]

#set up counter

score = 0 #the 0 is a integer +1 as the score goes on to calculate the final
used_items = [] #this is a list to store all of the plastic items

#Ask questions using a while loop

i = 0
while i < len(questions):
    answer = input(questions[i])
    if answer == "yes":

        # add item to used list

        used_items.append(items[i])
        # increasing the score everytime the user says yes
        score = score + 1
        i = i + 1 #moving on to the next question
    elif answer == "no":
        i = i + 1 #moving on to the next question
    else:
        print("You can only answer with yes or no")

    #display the score
    print (name +  " you used " + str(score) + " plastic items today.")
    print()

#showing plastic items using the for loop
if len(used_items) > 0: #
    print("Plastic items used:")
j = 0
while j < len(used_items):
    print(used_items[j])
    j = j + 1

else:
    print("Great job you didnt use any plastic items today")

#feedback based off of the score
if score == 0:
    print(" You are a EcoHero! You are helping save the planet")
elif score <= 2:
    print(" Good job you are right on track.")
elif score <= 4:
    print (" You are doing olay but you have to use less plastic")
else:
    print("You've used a dangerous amount of plastic use less!")

#ending quiz display
print("Thank you for using the eco quiz" + name)



