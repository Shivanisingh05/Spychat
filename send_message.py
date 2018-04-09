from steganography.steganography import Steganography
from select_friend import select_a_friend
from datetime import  datetime
from spy_details import  *
import csv


def send_message():
    #
    friend_choice = friends[select_a_friend()].name
    original_image = raw_input("Enter the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("Enter your secret message. ")
    Steganography.encode(original_image, output_path, text)
    # Successful message after encoding
    print("Encryption successfully!!")
    # the message will be stored in chat message class
    new_chat = ChatMessage(spy_n= spy.name, friend_n= friend_choice, time= datetime.now().strftime("%d %B %Y"), message=text)

    # name of the friend along which we add message.
    chats.append(new_chat)
    print("your secret message is ready.")
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat.spy_n, new_chat.friend_n, new_chat.time, new_chat.message])





