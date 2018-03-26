from add_status import add_status_messages
import spy_details

def start_chat(spy_name, spy_age, spy_rating):  # currently not using the parameters
    continue_option = "Y"
    while (continue_option == 'Y' or continue_option == 'y'):
        current_status_messesge = None
        print("your current status is " + str(current_status_messesge))
        menu_option = int(input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        while (menu_option<=6):
            if menu_option == 1:
                print("You choose update the status ")
                current_status_messesge = str(add_status_messages(current_status_messesge)) # calls the add_status_message from the add_status file
                print("Your selected status is:" + current_status_messesge) #Displays the status chosen or entered by the spy
                break
            elif menu_option == 2:
                print("Adding a friend initiated......")
                break
            elif menu_option == 3:
                print("Send a secret message initiated......")
                break
            elif menu_option == 4:
                print("Read a secret message initiated......")
                break
            elif menu_option == 5:
                print("Reading chat from user")
                break
            elif menu_option ==6:
                print("Exiting now.....")
                exit()
        continue_option = input("Would you like to perform another operation (Y/N)")
    print("Thank you for your time")


spy_is_online = False  # status of the spy
user_option = input(
    "Would you like to continue as a default user (default) or create your own (new)? ")  # type of user
# -------------------------------------------------------------------------------------------------
# for creating new user
# -------------------------------------------------------------------------------------------------
if user_option == "new":
    spy_name = input("Welcome to SpyChat, you must tell me you Spyname first:")
    if len(spy_name) > 0: # to calculate the length of the string
        print('Welcome ' + spy_name + ' Glad to have you with us.')
        spy_salutation = input("What should I call you Mr. or Ms. ?")
        print(
            'Alright ' + spy_salutation + '.' + spy_name + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(input('What is your age? '))  # age of the spy
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input('What is your spy rating? '))
        if spy_rating > 4.5:
            print('Great Ace!')
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
        print('Sorry you are not of the correct age to become a spy.')  # entered age is not between 12 and 50
    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your sp rating is " + str(
            spy_rating))  # float value to string value
    spy_is_online = True
    print('Changing the status of spy from offline to online ' + str(
        spy_is_online))  # bool value to string value for concatenation
    start_chat(spy_name, spy_age, spy_rating)  # calling menu option
# -----------------------------------------------------------------------------------------------------------------------
# for continuing as a default user
# -----------------------------------------------------------------------------------------------------------------------
elif user_option == 'default':

    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_details.spy_salutation + '.' + spy_details.spy_name + ", Your sp rating is " + str(
            spy_details.spy_rating))  # float value to string value
    spy_is_online = True

    start_chat(spy_details.spy_name, spy_details.spy_age, spy_details.spy_rating)  # calling menu option
else:
    print("Please select default user or create a new one.")