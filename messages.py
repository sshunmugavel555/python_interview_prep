def show_messages(msgs):
    """ Greets everyone from the input list argument """
    for msg in msgs:
        print(f"{msg.title()}")


def send_messages(msgs,sntmsgs):
    """ Print and move msgs from msg list to sent message list """
    while msgs:
        msg=msgs.pop()
        print(f"{msg}")
        sntmsgs.append(msg)
    
    return sntmsgs
    
msgList=['how are ya','wassup yo','yo jo']
sntmsgs=[]

sent_msgList=send_messages(msgList[:],sntmsgs)

for eachSent in sent_msgList:
    print(eachSent)

print(msgList)


