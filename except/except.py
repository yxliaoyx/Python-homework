import logging

try:
    with open('ch6ex1.txt') as fp:
        # 資料格式為 字串, 整數, 整數, 0或1
        for index, line in enumerate(fp):
            item = line.split(',')
            try:
                list(item[0])
            except BaseException as err:
                print('第{}筆資料，第0個欄位'.format(index))
                print(err)

            try:
                int(item[1])
            except BaseException as err:
                print('第{}筆資料，第1個欄位'.format(index))
                print(err)

            try:
                int(item[2])
            except BaseException as err:
                print('第{}筆資料，第2個欄位'.format(index))
                print(err)

            try:
                if int(item[3]) == 0 or int(item[3]) == 1:
                    raise ValueError('資料格式錯誤(0或1)')
            except BaseException as err:
                print('第{}筆資料，第3個欄位'.format(index))
                print(err)

# 檔案開啟失敗
except FileNotFoundError as err:
    logging.error(err)
