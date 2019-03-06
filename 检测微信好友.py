# encoding:utf-8
import itchat
import time
itchat.auto_login(hotReload=True)
itchat.run()
friends = itchat.get_friends(update=True)[1:]
print(friends)
for i,f in enumerate(friends):
    i += 1
    print('正在检测第{0}/{1}位好友,昵称:{2}'.format(i,len(friends),f['UserName']))
    itchat.send('Python Auto Send! జ్ఞ ా',toUserName=f['UserName'])
    time.sleep(3)
print('测试完毕，请打开手机客户端查看结果，欢迎下次使用')