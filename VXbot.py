# encoding:utf-8
# 2018/11/26
import itchat
import requests
import re
def get_songlink(name):
    response = requests.get("http://sou.kuwo.cn/ws/NSearch?type=music&key={0}".format(name)).text
    songinfo = re.compile(
        '<a href="http://www.kuwo.cn/yinyue/(\d+)/" title="(.*?)" target="_blank">.*?<p class="s_name"><a href="http://www.kuwo.cn/mingxing/.*?/" target="_blank" title="(.*?)">',
        re.S).findall(response)
    songid = songinfo[0][0]
    songname = songinfo[0][1]
    songer = songinfo[0][2]
    # 下载链接
    song_res = requests.get(
        "http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid={0}&type=convert_url&response=res".format(songid)).url
    return str(song_res)
@itchat.msg_register([itchat.content.TEXT,itchat.content.NOTE],isGroupChat=True)
def chatlog(msg):
    chatroom_ids = msg['FromUserName']
    username = msg['ActualNickName']
    tousername = msg['ToUserName']
    print(chatroom_ids)
    if msg['Type'] == itchat.content.TEXT:
        content = msg['Content']
        print("{0}说:{1}".format(username, content.strip()))
        if "歌曲" in content:
            songname = re.findall(r'歌曲(.*)',content)[0]
            print(songname)
            itchat.send_msg(get_songlink(songname),toUserName=tousername)
    elif msg['Type'] == itchat.content.SHARING:
        content = msg['Text']
        print("{0}说:{1}".format(username, content.strip()))
        if "歌曲" in content:
            songname = re.findall(r'歌曲(.*)',content)[0]
            print(songname)
            itchat.send_msg(get_songlink(songname),toUserName=tousername)

itchat.auto_login(hotReload=True,enableCmdQR=1)
itchat.run()
# for friends in itchat.get_friends(update=True):
#     # print(friends)
#     info = '''
#     微信id:{0}
#     昵  称:{1}
#     城  市:{2}{3}
#     备  注:{4}
#     性  别:{5}
#     个  签:{6}
#     =======================================
#     '''.format(friends['UserName'],friends['NickName'],friends['Province'],friends['City'],friends['RemarkName'],friends['Sex'],friends['Signature'].strip())
    # print(info)
# for chatrooms in itchat.get_chatrooms(update=True)[1:]:
#     chatname = chatrooms['NickName']
#     print("群昵称:{0}\n成员列表\n==============".format(chatname))
#     # print(itchat.search_chatrooms(userName=chatrooms['UserName']))
#     for members in itchat.search_chatrooms(userName=chatrooms['UserName'])['MemberList']:
#         print("微信id:{0}\n昵  称:{1}".format(members['UserName'],members['NickName']))

