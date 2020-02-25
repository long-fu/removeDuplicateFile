# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import hashlib
import io

# 需要遍历的目录
root_url = ""

# 
file_path_list_str = []
# 文件md5值 前面512K文件值
file_md5_list_str = [] 

# 字典
remove_file_url_list_tup = [] #(path,21)


def remove_file(url_str):
    print("删除文件",url_str)

    if os.path.isfile(url_str):

        if os.path.exists(url_str):
            
            os.remove(url_str)

            return True
    
    return False

def path_isfile(path_srt):
    if os.path.isfile(path_srt):
        if os.path.exists(path_srt):
            return True
    return False

def raw_md5(str_byte):
    str_md5 = hashlib.md5(str_byte).hexdigest()
    return str_md5

def raw_file_md5(path_srt):
    out_size = 1024
    if path_isfile(path_srt):
        size = os.path.getsize(path_srt)
        with io.open(path_srt,mode='rb') as fw:
            # res_b = b""
            if size > out_size:                
                res_b = fw.read(out_size)
                fw.close()
                return (path_srt,raw_md5(res_b),size)
            else:
                res_b = fw.read()
                fw.close()
                return (path_srt,raw_md5(res_b),size)
    return ("","",0)
    

def check_floder_url(url_str):
    pass
    return True

def file_path_list(floder_str):
    for root, dirs, files in os.walk(floder_str):
        # print(root,"--",dirs,"--",files,'\r\n')
        # print(root, "consumes", end="\r\n")
        for name in files:
            file_path = os.path.join(root,name)
            file_path_list_str.append(file_path)
    return file_path_list_str

if __name__ == "__main__":
    floder_url = ""
    while True:
        floder_url = #input("请输入需要检查的地址: \n退出请输入q\n")
        if floder_url == "":
             print("请输入需要检查的地址")
             continue
        elif floder_url == "q":
            exit("强制退出")
        elif check_floder_url(floder_url) == False:
            print("地址输入错误,请重新输入地址")
            continue
        else :
            print("最后需要检查的地址",check_floder_url)
            break
    file_path_list_str = file_path_list(floder_url)
    print("需要操作多少文件",len(file_path_list_str))
    for path_str in file_path_list_str:
        md5_tup = raw_file_md5(path_str)
        if md5_tup[2] > 0:
            if md5_tup[1] in file_md5_list_str:
                remove_file_url_list_tup.append(md5_tup)
                pass
            else:
                file_md5_list_str.append(md5_tup[1])
        else:
            continue
    # print(remove_file_url_list_tup, end="\r\n")
    for item in remove_file_url_list_tup:
        # print(item,end="\r\n")
        remove_file(item[0])
    print("总共存在多少重复文件",len(remove_file_url_list_tup))

