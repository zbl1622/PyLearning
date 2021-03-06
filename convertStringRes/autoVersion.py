# 对比两个目录，如果目录下内容有变化，则info.json中的version数值+1
"""
使用方法：
使用git分别拉取项目到两个不同的目录下，
其中一个检出到最新的发布版本，另一个检出到上一次发布的版本
在脚本头部修改配置，运行脚本
"""

import os
import hashlib
import json

rootPath = "D:/WorkProjects"
oldPath = rootPath + "/SmartHomeV6Code_H5_old"  # 上一次发布的版本
newPath = rootPath + "/SmartHomeV6Code_H5"  # 最新发布版本
folderList = ["addDevice", "chatWebSocket", "default", "device/*", "editScene", "houseKeeper1", "ManagerGateWay",
              "SMSNotification", "source"]  # 需要比较的一级目录

update_file_list = []


# return False表示目录内容不同，True表示目录内容相同
def compare_path(o_path, n_path, deep):
    if n_path.endswith("info.json") and deep == 1:
        # print("遇到info.json跳过")
        return True
    if (not os.path.exists(o_path)) and os.path.exists(n_path):
        print("旧目录不存在:" + o_path)
        if deep == 0:
            update_infojson(o_path, n_path)
        return False
    if os.path.exists(o_path) and (not os.path.exists(n_path)):
        print("新目录不存在:" + n_path)
        return False
    if os.path.exists(o_path) and os.path.exists(n_path):
        if os.path.isfile(n_path):
            result = get_file_md5(o_path) == get_file_md5(n_path)
            if not result:
                if deep == 0:
                    update_infojson(o_path, n_path)
                print("文件不一样:" + n_path)
            return result
        else:
            for c_path in os.listdir(n_path + "/"):
                result = compare_path(o_path + "/" + c_path, n_path + "/" + c_path, deep + 1)
                if not result:
                    if deep == 0:
                        update_infojson(o_path, n_path)
                    return False
        return True
    return True


def update_infojson(o_root_path, n_root_path):
    update_file_list.append(n_root_path)
    print("升级目录下info文件:" + n_root_path)
    read_info_file_path = o_root_path + "/info.json"
    write_info_file_path = n_root_path + "/info.json"
    # 读取旧目录下info.json中的version
    version = 1
    try:
        infojson = None
        if not os.path.exists(read_info_file_path):
            infojson = json.loads("{\"version\":0}")
        else:
            infojson = json.loads(open(read_info_file_path, "r").read())
        version = infojson["version"] + 1
        infojson_string = json.dumps(infojson)
        print("info.json:" + infojson_string)
        if not os.path.exists(write_info_file_path):
            os.makedirs(write_info_file_path)
        infojson["version"] = version
        infojson_string = json.dumps(infojson)
        file = open(write_info_file_path, "w+")
        file.write(infojson_string)
    except:
        print("info.json操作发生错误:" + n_root_path)
        pass


def get_file_md5(filename):
    if not os.path.isfile(filename):
        return
    md5 = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        md5.update(b)
    f.close()
    return md5.hexdigest()


update_file_list.clear()
for path in folderList:
    if path.endswith("/*"):
        print("获取子目录列表并且比较:" + path)
        for child_path in os.listdir(newPath + "/" + path[:-1]):
            print("子目录比较:" + child_path)
            compare_path(oldPath + "/" + path[:-1] + child_path, newPath + "/" + path[:-1] + child_path, 0)
    else:
        print("目录比较:" + path)
        compare_path(oldPath + "/" + path, newPath + "/" + path, 0)

print("\n\n升级目录列表:")
for folder_name in update_file_list:
    print(folder_name)
