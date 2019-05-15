# encoding:utf-8
from PIL import Image
import argparse

#�����������������
parser = argparse.ArgumentParser()

parser.add_argument('file')     #�����ļ�
parser.add_argument('-o', '--output')   #����ļ�
parser.add_argument('--width', type = int, default = 80) #����ַ�����
parser.add_argument('--height', type = int, default = 80) #����ַ�����

#��ȡ����
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# ���Ƕ���Ĳ��ظ����ַ��б��Ҷ�ֵС�����������б�ͷ�ķ��ţ��Ҷ�ֵ�����������б�ĩβ�ķ���
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("01")

# ��256�Ҷ�ӳ�䵽70���ַ���
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    #��ͼƬ���������ص���ɵĶ�ά���飬i����ÿһ�У�j����ÿһ��
    for i in range(HEIGHT):
        for j in range(WIDTH):
            #getpixel()�����Ĳ�������ÿ�����ص���ͼƬ�е����λ�ã�w��h����ɵ�Ԫ��
            #����ֵ��һ������ͼƬ����ֵ��(r,g,b,alpha)Ԫ��
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #�ַ���������ļ�
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)