from spy_details import User, friends


def add_friend():
    # using class user in spy_details
    n_friend = User(" ", " ", 0, 0.0)

    # ask user for name
    n_friend.name = input("Please add your friend's name: ")

    # user name validation.
    if len(n_friend.name) > 0:
        if len(n_friend.name) > 20:
            print("Your name length is big.")
    else:
        print("Name should be not empty or length is less then 20 char.")
        return add_friend()

    n_friend.salutation = input("What to call Mr. or Ms.?: ")

    # user salutation validation
    if len(n_friend.salutation) > 0:
        if len(n_friend.salutation) > 5:
            print("Your salutation is too big.")
    else:
        print("Salutation empty or check length")
        return add_friend()

    # concatination for full name
    n_friend.name = n_friend.salutation + " " + n_friend.name

    # ask for age of friend
    n_friend.age = int(input("Age: "))

    if 12 < n_friend.age < 50:
        True
    else:
        print("Age should be in between 12 to 50")
        return add_friend()

    #ask for rating of friend, using float
    n_friend.rating = float(input("Spy rating? "))

    if n_friend.rating > 0.0:
        True
    else:
        print("Ratting should be more than 0.0")
        return add_friend()

    # add friend if all conditions check
    friends.append(n_friend)
    print('Friend Added!')

    # check total no of friends in a list.
    return len(friends)