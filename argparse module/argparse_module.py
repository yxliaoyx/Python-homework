# 當命令列為python web.py
# 開啟http://www.ntou.edu.tw
# 
# 當命令列為python web.py -u https://docs.python.org/
# 開啟https://docs.python.org/
import webbrowser
import argparse

parser = argparse.ArgumentParser(description='開啟網頁')
parser.add_argument("-u", "--url", default='http://www.ntou.edu.tw')

args = parser.parse_args()
webbrowser.open(args.url)
