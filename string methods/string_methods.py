s = "python,programming,language"
# 判斷"pro"是否在s裡, True
print("pro" in s)

# 回傳"prog"在s的位, 7
print(s.find("prog"))

# 回傳s用","分隔的list, ['python', 'programming', 'language']
print(s.split(","))

# 用"-"把第一個和第二個字串join起來, python-programming
print("-".join(s.split(",")[0:2]))

# 判斷s的開頭是否是"py", True
print(s.startswith("py"))

# 判斷s的結尾是否是"age", True
print(s.endswith("age"))

# 轉大寫, PYTHON,PROGRAMMING,LANGUAGE
print(s.upper())

# 每個單字自首大寫, 其餘為小寫, Python,Programming,Language
print(s.title())

# 判斷s是否是alphabetic ASCII characters, False
print(s.isalpha())

# 把"programming"替換成"interpreted", python,interpreted,language
print(s.replace("programming", "interpreted"))
