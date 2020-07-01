# Python Spider 爬虫
web spider 网络爬虫项目练习

## 以下内容仅作技术研究

## PC端
### [百度百科]
通过关键字，获取百科中关键字的基本解释
### [图片下载]
下载次元岛(http://ciyuandao.com/) 中的图片保存到本地
### [墨迹天气]
通过网页版墨迹天气，获取目标城市的基础天气信息
### [qq群成员获取（未完善）]
获取指定群中所有群友的昵称和账号，目前需要手动获取加密参数值以及cookie，后续优化扫码登陆获取，支持导出csv格式的文件


## 移动端
### [皮皮虾app]
由于内涵段子关闭，无奈之下，只能抓取手机app皮皮虾中的内容
### [黄历]
作者用的是vivo，手机中自带一些小程序(快应用)，抓取了黄历中的相关信息（五行等）
### [互动百科]
互动百度是手机中自带的快应用，和百度百科作用一致，获取关键字的基本解释
### [小橘句子]
获取小程序小橘句子中的语句
### [抖音视频下载]
抖音视频无水印下载


## 小工具
### [微信清理非好友联系人]
本程序采取的itchat这个好用第三方微信库，通过向每个联系人发送特殊字符，已达到获取已经不是好友关系的联系人，最终结果将会在移动端显示
### [微信批量申请添加好友（慎用）]
这个工具是批量申请添加群聊中的人，由于微信限制，谨慎使用，可能会导致封号
### [QQ轰炸机]
通过调用系统接口，获取聊天窗口句柄，模拟按键来实现轰炸的效果（仅供技术交流）
### [图片去重]
通过递归的方法去获取一个文件夹中的所有图片，利用hash进行去重
### [m3u8文件链接提取（未完善）]
通过m3u8文件的下载链接，获取文件中的视频链接，利用多线程进行下载，后续需要增加合并视频的功能
### [windows版本计划任务]
在windows上实现定时任务，目前版本的缺点是只能是当日，且时间不能小于当前时间

[百度百科]:https://github.com/Jruing/Python-Spider/blob/master/baike.py
[图片下载]:https://github.com/Jruing/Python-Spider/blob/master/cosplay.py
[墨迹天气]:https://github.com/Jruing/Python-Spider/blob/master/weather_moji.py
[qq群成员获取（未完善）]:https://github.com/Jruing/Python-Spider/blob/master/qq%20%E7%BE%A4%E6%88%90%E5%91%98%E8%8E%B7%E5%8F%96.py
[皮皮虾app]:https://github.com/Jruing/Python-Spider/blob/master/pipixia_spider.py
[抖音视频下载]: https://github.com/Jruing/Python-Spider/blob/master/抖音无水印视频下载.py
[黄历]:https://github.com/Jruing/Python-Spider/blob/master/%E9%BB%84%E5%8E%86%EF%BC%88%E5%BF%AB%E5%BA%94%E7%94%A8%EF%BC%89.py
[互动百科]:https://github.com/Jruing/Python-Spider/blob/master/%E4%BA%92%E5%8A%A8%E7%99%BE%E7%A7%91%EF%BC%88%E5%BF%AB%E5%BA%94%E7%94%A8%EF%BC%89.py
[小橘句子]:https://github.com/Jruing/Python-Spider/blob/master/%E5%B0%8F%E6%A9%98%E5%8F%A5%E5%AD%90%EF%BC%88%E5%B0%8F%E7%A8%8B%E5%BA%8F%EF%BC%89.py
[微信清理非好友联系人]:https://github.com/Jruing/Python-Spider/blob/master/%E6%A3%80%E6%B5%8B%E5%BE%AE%E4%BF%A1%E5%A5%BD%E5%8F%8B.py
[微信批量申请添加好友（慎用）]:https://github.com/Jruing/Python-Spider/blob/master/wx_add_friends.py
[QQ轰炸机]:https://github.com/Jruing/Python-Spider/blob/master/qq%E8%BD%B0%E7%82%B8%E6%9C%BA.py
[图片去重]:https://github.com/Jruing/Python-Spider/blob/master/md5%E5%9B%BE%E7%89%87%E5%8E%BB%E9%87%8D.py
[m3u8文件链接提取（未完善）]:https://github.com/Jruing/Python-Spider/blob/master/m3u8.py
[windows版本计划任务]:https://github.com/Jruing/Python-Spider/blob/master/windows%E7%89%88%E6%9C%AC%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1.py
