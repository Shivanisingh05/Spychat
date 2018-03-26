from spy_details import STATUS_MESSAGES

# add_status() function is use to add status like in whatsapp
def add_status_messages(current_status_message):
    if current_status_message !=None:
        print ("your current status is:"+current_status_message)
    else:
        print ("you don't have any current messeage")
    question=input("do you want to select status from old status? y/n")
    # if user want to add new status
    # then append new_status to STATUS_MESSAGE
    if question.upper()=="N":
        new_status=input("enter your new status ")
        if len(new_status)>0:
            STATUS_MESSAGES.append(new_status)
            return(new_status)
        else:
            print ("invalid new status need to be enter ")
    # if user want to select from STATUS_MESSAGE
    elif question.upper()=="Y":
        # showing all old status
        for i in range(len(STATUS_MESSAGES)):
            print (str(i)+"."+STATUS_MESSAGES[i])
        message_selection=int(input("\n choose from above status"))
        # if user enter more than the no of  status in STATUS MESSAGE
        if len(STATUS_MESSAGES)>message_selection:
            update_status_message=STATUS_MESSAGES[message_selection]
        else:
            print ("selected message is not in older status ")
        return update_status_message