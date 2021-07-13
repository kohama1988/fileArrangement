import os,shutil,re,csv
from datetime import datetime

base = ['03100_フォルダー管理ルール', '03100_海外支援要請書', '03101_契約書', '03109_棚卸管理表', 'ルール違反フォルダー&ファイル']
wrong_f = './TEST/ルール違反フォルダー&ファイル'
root = './TEST'

f = open('moved.csv','w+',newline='')
csvWriter = csv.writer(f)
# 第3階層のルール違反ファイルを「ルール違反フォルダー&ファイル」に移動
for item in os.listdir(root):
    if item not in base:
        f_path = os.path.join(root,item)
        csvWriter.writerow([os.path.abspath(f_path),datetime.now()])
        shutil.move(f_path,wrong_f)

#　第4階層のルール違反ファイルを「ルール違反フォルダー&ファイル」に移動
for path3cls in os.listdir(root):
    if path3cls != 'ルール違反フォルダー&ファイル':
        for item in os.listdir(os.path.join(root,path3cls)):
            fPath = os.path.join(root,path3cls,item)
            # print(fPath,': ',os.path.isdir(fPath))
            if os.path.isfile(fPath) or not re.search(r'[12]\d{3}年',item):
                csvWriter.writerow([os.path.abspath(fPath),datetime.now()])
                shutil.move(fPath, os.path.join(wrong_f,path3cls,item))

#　第5階層のルール違反ファイルを「ルール違反フォルダー&ファイル」に移動
for path3cls in os.listdir(root):
    if path3cls != 'ルール違反フォルダー&ファイル':
        for item in os.listdir(os.path.join(root,path3cls)):
            fPath = os.path.join(root,path3cls,item)
            if os.path.isdir(fPath):
                for path5cls in os.listdir(fPath):
                    path5 = os.path.join(fPath,path5cls)
                    if not re.search(r'^[12]\d{7}_',path5cls):
                        csvWriter.writerow([os.path.abspath(path5),datetime.now()])
                        shutil.move(path5,os.path.join(wrong_f,path3cls,item,path5cls))

f.close()
