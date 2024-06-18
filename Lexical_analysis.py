# -*- coding: utf-8 -*-

#####标识符#######
# Python 3.0 引入了 ASCII 之外的更多字符（请参阅 PEP 3131）。这些字符的分类使用 unicodedata 模块中的 Unicode 字符数据库版本。标识符的长度没有限制，但区分大小写。

def print_unicode(codepoint: str = None):
    if codepoint is None:
        # 读取文件内容
        with open('PropList-13.0.0.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        unicode_info = {}
        current_category = ""

        # 提取Unicode字符信息
        for line in lines:
            if line.strip() == "":
                continue
            if line.startswith("#"):
                current_category = line.strip("#").strip()
            else:
                parts = line.split(";")
                if len(parts) >= 2:
                    codepoint_range = parts[0].strip()
                    category = parts[1].strip().split()[0]
                    unicode_info[codepoint_range] = {
                        "category": category, "description": current_category}

        # 打印提取到的Unicode字符信息及对应字符
        for codepoint_range, info in unicode_info.items():
            try:
                    start, end = codepoint_range.split("..")
            except Exception as e:
                    pass
            start_codepoint = int(start, 16)
            end_codepoint = int(end, 16)

            characters = [chr(codepoint)
                                for codepoint in range(start_codepoint, end_codepoint + 1)]
            character = ''
            for char in characters:
                character = character + " " + char
            print(
                f"Codepoint Range: {codepoint_range} | Category: {info['category']} | Characters: {character}")
    else:
        print('Codepoint: %s is %s' % (codepoint, chr(int(codepoint, 16))))


print_unicode('110BD')



# a = 4.54
# b = 'haha'
# print(f'%s的年龄是%d' % (b,a))
# print('%(language)s has %(number)#x  quote types.' %
#       {'language': "Python", "number": 2})
