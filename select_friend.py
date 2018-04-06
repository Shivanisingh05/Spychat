from spy_details import friends

0# select friend from friend list.
def select_a_friend():

    # indexing position.
    counter = 1

    # to select a friend with indexing
    for friend in friends:
        print(str(counter) + ". " + friend.name + " Age : " + str(friend.age))

        counter = counter + 1       # access all list.

    # ask user to select friend.
    friend_choice = int(raw_input("\nPlease select from the given list : "))
    #  selected friend to perform action
    friend_choice_position = int(friend_choice) - 1
    # Check if user has out of index choice.
    if friend_choice_position + 1 > len(friends):
        print("Sorry, this friend is not present.")
        exit()
    else:
        # returns the selected friend to perform actions
        print("You have selected %s with index %d!" % (friends[friend_choice_position].name, friend_choice_position))
        return friend_choice_position