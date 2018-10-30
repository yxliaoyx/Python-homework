import sys

even, odd = 0, 0

for line in sys.stdin.readlines():
    int_line = int(line)
    if int_line % 2:
        odd += int_line
    else:
        even += int_line

print('odd:{} even:{}'.format(odd, even))
