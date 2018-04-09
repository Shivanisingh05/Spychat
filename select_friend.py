from spy_details import friends

# select friend from friend list.
def select_a_friend():


    counter = 1
    for new_friend in friends:
        print(str(counter) + ". " + new_friend.name + " Age : " + str(new_friend.age))

        counter = counter + 1
    friend_choice = int(raw_input("\nPlease select from the given list : "))
    friend_choice_position = int(friend_choice) - 1
    #  selected friend to perform action
    if friend_choice_position + 1 > len(friends):
    #if len(friends)<(friend_choice):
        print ("You have no such friend.")
        exit()
    else:
        print("You have selected %s with index %d!" % (friends[friend_choice_position].name, friend_choice_position))
        return friend_choice_position



