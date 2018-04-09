from add_status import status_message
from send_message import send_message
from add_friend import add_friend
from read_message import read_message
from spy_details import *
from termcolor import colored
from select_friend import select_a_friend
import csv

# function for reading chats
def read_chats(choice):

    choose = friends[choice].name
    with open('chats.csv', 'rU') as chats_data:
     read = csv.reader(chats_data)
     for row in read:
        try:
            c = ChatMessage(spy_n=row[0], friend_n=row[1], time=row[2], message=row[3])
            # checking the chats of the current spy with selected friend
            if c.spy_n == spy.name and c.friend_n == choose:
                print colored("The message is sent to: %s " % choose, "red")
                print colored("On Time: [%s]" % c.time, "blue")
                print("Message is: %s" % c.message)
                return 1
        except IndexError:
            pass
        continue

def start_chat(name, age, rating):
    from spy_details import current_status_message

    # for loading friends
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=(row[1]), age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # for loading chats
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_n=row[0], friend_n=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    if not age > 12 and age < 50:
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print(error_message)
    else:
        # if authentication complete
        # show all the spy details.
        welcome_message = "Authentication complete. Welcome\n\n" \
                          "Name : " + name + "\n" \
                                             "Age: " + str(age) + "\n" \
                                                                  "Rating: " + str(rating) + "\n" \
                                                                                        "Proud to have you on board\n"
        print(welcome_message)

        # displaying menu for user.
    load_friends()
    load_chats()

    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n " \
                   "2. Add a friend \n 3. Send a secret message \n " \
                   "4. Read a secret message \n 5. Read chats from a user \n 6. Close application \n"
        menu_choice = int(raw_input(menu_choices))

        if menu_choice == 1:
            print('status')
            current_status_message = status_message(current_status_message)
        elif menu_choice == 2:
            # add a new friend
            number_of_friends = add_friend()
            print('You have %d friends' % number_of_friends)

        elif menu_choice == 3:
            # send a secret message
            print('send a secret message:')
            send_message()

        elif menu_choice == 4:
            # read the secret message sent by friend
            print('Read secret msg')
            read_message()

        elif menu_choice == 5:
            # read the chat history
            print('Read chats form a user')
            print("For which user do you want to read chats?")
            choice = select_a_friend()
            read_chats(choice)

        elif menu_choice == 6:
            # close application
            print('close application')
            show_menu = False

        # if user chooses other than menu choices.
        else:
            print("wrong choice try again.")
            exit()