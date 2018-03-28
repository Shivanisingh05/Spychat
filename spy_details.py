####### Default User #######
# default status

current_status_message = None

# default status list
status = ['My name is Shivani Singh.', 'I am student of Acadview.', 'Location: New Delhi']

class User:
    # creating class
    def __init__(self, uname, salutation, age, rating):
        self.uname = uname
        self.salutation = salutation
        self.age = age
        self.rating = rating


# define user_name, age, rating
default = User('Shivani Singh', 'Ms.', 20, 4.3)


# details of some existing friends
friend_one = User('Neetu', 'Ms.', 21, 4.5)
friend_two = User('Nancy', 'Ms.', 20, 3.9)
friend_three = User('Kuldeep', 'Mr.', 21, 3.7)

# lists of friends
friends = [friend_one, friend_two, friend_three]