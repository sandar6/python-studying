import time
import itchat



def getheadimg():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[0:]
    for i in friends:
        if i['RemarkName'] == "姜颖":
            username = i['UserName']
            imgdate = itchat.get_head_img(userName=username)
            with open('size.txt') as f1:
                # print(f1.readlines()[-1].strip())
                if abs(len(imgdate) - int(f1.readlines()[-1].strip())) > 5:
                    # print(int(f1.readlines()[-1].strip()))
                    with open(r'小姜的换头像日常\{}.jpg'.format(time.strftime('%Y-%m-%d-%H-%M-%S')),'wb') as f2:
                        f2.write(imgdate)
                    with open('size.txt','a') as f3:
                        f3.write(str(len(imgdate))+'\n')


def getfriendsinfo():
    sing_list = []
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[0:]
    for i in friends:
        # print(i)
        if i['Sex'] == 2:
            signature = i['Signature']
            print(i['RemarkName']+'--->'+signature)
    #     if signature and ('span' not in signature):
    #         sing_list.append(signature)
    # text = "".join(sing_list)
    # print(text)

def chatroomdemo():
    itchat.auto_login(hotReload=True)
    chatrooms = itchat.get_chatrooms(update=True)[0:]
    for i in chatrooms:
        if i['NickName'] == '改名了叫侃大山':
            username = i['UserName']
            print(username)
            itchat.send_msg('下午好,{}'.format(time.strftime('%Y-%m-%d %X')),username)




if __name__ == '__main__':
    # getheadimg()
    # getfriendsinfo()
    chatroomdemo()