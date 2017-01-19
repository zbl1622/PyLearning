import os

rootPath = "D:/maitu_frame/"


def createAnimationFile(dirName):
    animationName = dirName
    path = rootPath + animationName

    animationFile = open(rootPath + "frame_anim_" + animationName + ".xml", 'w')
    animationFile.write(
        "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<animation-list xmlns:android=\"http://schemas.android.com/apk/res/android\" android:oneshot=\"false\">\n")

    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        # Newdir = os.path.join(path, "frame_rabbitbow" + number + filetype)  # 新的文件路径
        # os.rename(Olddir, Newdir)  # 重命名
        animationFile.write("<item android:drawable=\"@drawable/" + filename + "\" android:duration=\"60\" />\n")
    animationFile.write("</animation-list>")
    animationFile.close()


def findFile():
    filelist = os.listdir(rootPath)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(rootPath, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            filename = os.path.splitext(files)[0]  # 文件名
            createAnimationFile(filename)


findFile()
