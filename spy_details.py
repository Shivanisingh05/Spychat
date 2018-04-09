####### Information Of A Default User #######
# default status
current_status_message = None

# list of default status
status = ['My name is Shivani Singh.', 'Location: New Delhi']

########################################################################################################################
class Spy:
    # create class
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chat = []
        self.current_status_message = None
        self.count = 0
    ###################################################################################################################
class ChatMessage:
    def __init__(self, spy_n, friend_n, time, message):
        self.spy_n = spy_n
        self.friend_n = friend_n
        self.message = message
        self.time = time

# define user_name, age, rating
spy = Spy('Shivani Singh', 'Ms.', 20, 4.5)
friends = []
chats = []