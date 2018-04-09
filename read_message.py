from steganography.steganography import Steganography
from spy_details import  *
from select_friend import select_a_friend
from datetime import datetime
import csv
from termcolor import colored


def read_message():
    sender = select_a_friend()

    output_path = raw_input("Enter the name of the file?")
    secret_text = Steganography.decode(output_path)
    print(secret_text)
    words = secret_text.split()
    for i in words:
        if i == "SOS" or i == "sos" or i == "save" or i == "help" or i == "Emergency" or i == "danger":
            # Maintain the average number of words spoken by a spy every time a message is received from a particular spy.
            friends[sender].count += len(words)
            # Emergency alert
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow')),
            print(colored("!", 'grey', 'on_yellow'))

            # Help your friend by sending him a helping message
            print ("Don't panic !!")
            print ("I am coming to rescue.")

            # Adding the chat with the sender
            new_chat = ChatMessage(spy_n= spy.name, friend_n= sender, time= datetime.now().strftime("%d %B %Y"), message=secret_text)
            friends[sender].chat.append(new_chat)


        # When there was no case of emergency
        else:
            # Adding the chat with the sender
            new_chat = ChatMessage(spy_n=spy.name, friend_n=sender, time=datetime.now().strftime("%d %B %Y"), message=secret_text)
            friends[sender].chat.append(new_chat)
            print("Your secret message has been saved!")

        # Print the avg words spoken by your friend
        print "Average words said by",
        print(colored(friends[sender].name, 'red'))
        print "is",
        print(colored(friends[sender].count, 'red'))


        # Delete a spy from your list of spies if they are speaking too much
        if len(words) > 100:
            print(colored(friends[sender].name,'red'))
            print("Removed from friends list. What a chatter box! What a drag!!!")
            # Removes that chatterbox friend
            friends.remove(friends[sender])
    # When the image contains no secret message
    # 'TypeError' handling

        print("Nothing to decode from the image as it contains no secret message.")
    #-------------------------------------------------------------------------------------------------------------------
    new_chat = ChatMessage(spy_n=spy.name, friend_n=sender, time=datetime.now().strftime("%d %B %Y"),message=secret_text)
    print("Your secret message has been saved.")
    with open('chats.csv', 'a') as chats_records:
        write = csv.writer(chats_records)
        write.writerow([new_chat.spy_n, new_chat.friend_n, new_chat.time, new_chat.message])