#Collect user name and welcome the user

print("Welcome to the Eco Quiz!")
name = input("Enter your name:")
print (" Hello " + name)

#Define Questions about the issue/plastic polloution and state common plastic items

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
while i < length(questions):
    answer = input(questions[i])
    if answer == "yes":
        used_items.appnd(items[i])  # add item to used list
        score += 1  # increase the score every



