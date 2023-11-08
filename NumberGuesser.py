import random

#This code greets you.
hello_list = ["How are you?, Are you good?, Welcome"]
print(f"Hello_list: {hello_list}")

#This function prints a message to encourage people to play.
def letsplay():
    print("Lets Play!")
letsplay()

#Input any number from 1 to 100. 
player = int(input("Enter a number 1-100: "))
comp = random.randint(1, 100)
print(comp)

comp_down = 1
comp_up = 100


while comp != player:
   if comp > player:
    comp_up = comp - 1
    comp = random.randint(comp_down, comp_up)
    print(comp)
   if comp < player:
    comp_down = comp + 1
    comp = random.randint(comp_down, comp_up)
    print(comp)
   if comp == player:
       break