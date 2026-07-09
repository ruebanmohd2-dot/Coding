# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car
choice = int(input("Select Your Ride(1 for bike and 2 for Car)"))
# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"
if choice == 1:
    choice2 = int(input("1.Scooty or 2.Scooter "))
    if choice2 == 1:
        print("U have seleced scooty")
    if choice2 == 2:
        print("U have selected scooter")
# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"
elif choice == 2:
    choice3 = int(input("1.Sedan,2.SUV"))
    if choice3 == 1:
        print("You Have selected Sedan")
    if choice3 == 2:
        print("You Have selected SUV")
else:
    print("Wrong Choice")
# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"
