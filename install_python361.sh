#! /bin/sh
echo "============================================================="
echo "=====                欢迎使用本shell脚本                ====="
echo "=====                官网:Jruing.site                   ====="
echo "============================================================="
echo "当前目录:"`pwd`
# 安装Python所需依赖
echo `yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel`

# 安装Python3
if [ ! -f "./Python-3.6.1.tgz" ];then
echo "文件不存在"
echo`wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz`
echo `tar -zxvf Python-3.6.1.tgz`
cd Python-3.6.1
echo ./configure
echo make && make install
    if [! -f "~/.pip/pip.conf"];then
    echo "文件不存在"
    echo -e "[global]\nindex-url=https://pypi.douban.com/simple/" >> ~/.pip/pip.conf
    echo "豆瓣镜像源设置成功"
else
echo "文件已存在"
fi
