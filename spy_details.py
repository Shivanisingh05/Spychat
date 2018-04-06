####### Information Of A Default User #######
from datetime import datetime

# default status
current_status_message = None

# list of default status
status = ['My name is Shivani Singh.', 'Location: New Delhi']


class Spy:
    # create class
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# define user_name, age, rating
spy = Spy('Shivani Singh', 'Ms.', 20, 4.5)


# details of some existing friends
friend_one = Spy('Ujjwal', 'Mr.', 21, 3.1)
friend_two = Spy('Princi', 'Ms.', 20, 3.6)
friend_three = Spy('Vivek', 'Mr.', 20, 4.8)

# lists of friends
friends = [friend_one, friend_two, friend_three]