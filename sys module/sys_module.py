# 使用sys模組，讀入一連串整數(一列只有一個整數)直到EOF為止，輸出奇數的和與偶數的和
import sys

even, odd = 0, 0
# 輸入多行直到Enter + Ctrl-Z
for line in sys.stdin.readlines():
    int_line = int(line)
    if int_line % 2:
        odd += int_line
    else:
        even += int_line

print('odd:{} even:{}'.format(odd, even))
