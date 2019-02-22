import re

s1 = 'A12345A\nBA12345\nCADA\nA'
print("使用re.finditer('A',s1)找出每個A的位置")
for i in re.finditer('A', s1):
    print(i.group(), i.start())

print('使用re寫出找出s1裡在每一行開頭的A')
for i in re.finditer(r'\bA', s1):
    print(i.group(), i.start())

s2 = '(asd)sdasd)(asdsd)asdasd)(asdas)'
print("比較re.findall(r'\(.+\)',s2)與re.findall(r'\(.+?\)',s2)差別")
print(re.findall(r'\(.+\)', s2))
print(re.findall(r'\(.+?\)', s2))

s3 = '(1,234)5678(123)987(100,888,909)'
print('計算s3裡所有()裡的整數的和')
sum = 0
for i in re.findall(r'\((.+?)\)', s3):
    for j in i.split(','):
        sum += int(j)
print(sum)

s4 = '大雄有3隻羊2條狗，小明有狗3隻雞2隻，小花有1頭牛3隻豬2隻雞狗5條。'
print('使用re處理s4，抽取出相關資訊來計算大雄、小明、小花共有幾隻羊、狗、雞、豬、牛')
animal_list = re.findall(r'[羊狗雞豬牛]', s4)
count_list = re.findall(r'\d', s4)
animal_count_dict = {}
for i in range(len(animal_list)):
    if animal_list[i] in animal_count_dict:
        animal_count_dict[animal_list[i]] += int(count_list[i])
    else:
        animal_count_dict[animal_list[i]] = int(count_list[i])
print(animal_count_dict)
