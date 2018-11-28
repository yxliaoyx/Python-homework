import os
import datetime

# 輸入一個目錄，及n。列出此目錄(包含子目錄)下所有檔案modification time(os.path.getmtime)最多在n天內的檔案名稱

mypath = os.getcwd()
n = datetime.timedelta(1)

for root, dirs, files in os.walk(mypath):
    for f in files:
        fullpath = os.path.join(root, f)
        modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(fullpath))
        if datetime.datetime.now() - modification_time < n:
            print(f)
            print(modification_time)
