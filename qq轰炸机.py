# encoding:utf-8
import win32gui
import win32con
import win32clipboard as w
import time
import random
import linecache,os
def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 测试
#   模式一
def model_1():
    target = input("输入目标昵称：")
    # stop_time = int(input("输入间隔时间："))
    while True:
		# 发送的消息
        msg = ("我告诉你这样的情况你还需要明白了解的不是吗","我这埋汰你呢都是没速度和我继续的比拟呢不是奥妙。","我好象你爸爸似的你难道自己不清楚这样情况埃","你这样的蜗牛就是完全没什么速度反抗你爸爸我埃我可认为你这样的垃圾好象完全没什么力量似的","然后你完全没有力量你明白你的扣字垃圾吗。呵呵。废物。","我好象你爸爸似的随便殴打你这样的事实情况了埃我好象你爸爸似的。","不了解情况怎么的呢埃你为什么在这里耀武扬威。","现在了解什么情况你完全垃圾似的知道了没埃。","你好象垃圾似的你怎么和我对抗呢","呵呵你出来告诉我吗"," 然后你完全没有速度你明白什么情况吗，垃圾似的出来埃。","然后我随便殴打你这样的垃圾似的事实的不是吗。","你自己好象我儿子似的只能污蔑我还是怎么埃我这理解你是垃圾速度和我继续的比拟呢对吗。","我就是你父亲似的随便殴打你完全没什么力量似的。","父亲我随便殴打你这样的事实情况了啊弟弟。","难道不是那么出来我现在不随便殴打你吗青年 ","你自己现在不了解什么还是怎么殴打飞机的爸爸,我怎么感觉你和我没脾气的儿子是的反抗爸爸的,儿子你现在自己怎么反抗的爸爸的难道什么情况啊,我怎么国家你和我没脾气的儿子是的什么殴打 现在的你看见你爹的各种速度害怕了还是怎么的 ","孩子你现在的可有意思了吗你明白什么情况了吗","小伙子啊爸爸随意的打的你了啊你明白什么情况。","你就是完全没什么力量反抗我还是怎么啊弟弟。","你自己不了解情况还是怎么的你完全垃圾似的")
        send_qq(target, random.choice(msg))
        # time.sleep(stop_time)
#   模式二
def model_2():
    target = input("输入目标昵称：")
    # stop_time = input("输入间隔时间：")
    data = []
    file = open('msg.txt','r')
    text = file.readlines()
    print(text)
    if os.path.exists('msg.txt') == True:
        while True:
            for i in text:
                if i == '\n':
                    pass
                else:
                    data.append(i)
            send_qq(str(target), random.choice(data))
            time.sleep(3)
    else:
        print('文件不存在')
    
if __name__ == '__main__':
    print('''
    =================选择攻击模式=================
    1：使用程序自带的攻击句子
    2：使用本地文档
    3：q 退出
    ''')
    choice_model = input("输入攻击模式：")
    if choice_model == "1":
        model_1()
    elif choice_model == "2":
        model_2()
    elif choice_model == "q" or choice_model == 'q':
        print('谢谢使用')
        exit()
    else:
        exit()
