# Python 根Python 根据文件名新建文件夹并移动到文件夹里面据文件名新建文件夹并移动到文件夹里面
import os
import shutil


def main():
# 路径
    path = r"C:\Users\Administrator\Downloads\a"
    newPath = r"C:\Users\Administrator\Downloads\a\%s"


    for (root, dirs, files) in os.walk(path):
        for filename in files:
            singleFile = os.path.join(root, filename)
            res = os.path.splitext(filename)
            newFileDirs = newPath % (res[0]);
            if not os.path.exists(newFileDirs):
                os.mkdir(newFileDirs)
            shutil.move(singleFile, newFileDirs + "\\" + filename)


    pass


if __name__ == '__main__':
    main()