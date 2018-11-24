# encoding:utf-8
# 2018/4/3
# Author:Scar丶殇痕
import os
import time
os.system("color 0a")
print('''
        欢迎使用计划任务管理器   By：Scar丶殇痕
        
      注意：时间采用24小时制,计划时间不能小于当前时间 
            
          时间格式：例：13:14 即：1:14 PM
          
          = = = = = =程   序   列   表= = = = = =
          
          1.    开始程序
          
          2.    打开计划任务
          
          q.    退出

''')
for i in range(0,3):
    a = time.asctime()
    print("当前时间：{0}".format(a))
    cmd = input("输入命令：")
    if cmd == '1':
        work_name = input("输入计划任务的名称：")
        run_time = input("输入任务的运行时间：")
        file_path = input("输入运行文件的路径：")
        os.system('schtasks /create /sc once /TN {0} /ST {1} /TR {2}'.format(work_name,run_time,file_path))
    elif cmd == "2":
        os.system('taskschd.msc')
    else:
        print('谢谢使用！！！')
        break

