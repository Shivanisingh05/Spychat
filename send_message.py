from steganography.steganography import Steganography
from select_friend import select_a_friend
from spy_details import friends, Chat


def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("Enter the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("Enter your secret message. ")
    Steganography.encode(original_image, output_path, text)

    # for storing the message in chat message class
    new_chat = Chat(text, True)

    # along the name of friend with whom we add message
    friends[friend_choice].chats.append(new_chat)

    # Successful message after encoding
    print("Encryption successfully!!")

    # name of the friend along which we add message.
    friends[friend_choice].chats.append(new_chat)
    print("Secret message is ready.")