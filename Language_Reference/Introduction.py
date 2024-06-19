# -*- coding: utf-8 -*-

##### 1.2 Notation 标注#####
msg = """
在第二章词法分析的描述采用经过改进的 BNF 语法标注。看懂BNF词法才能看懂第二章。词法只是用于阅读官方文档。不涉及编程。python的BNF词法是变种的，和标准BNF词法稍有点区别。
另外BNF词法有点像正则的用法。
使用以下定义样式：
if_stmt ::=  "if" assignment_expression ":" suite
             ("elif" assignment_expression ":" suite)*
             ["else" ":" suite]
"""
print(msg)

nota_list = ['::=','|','*','+','[...]','(...)','<...>','\"...\"']

# 信息输入
def msginput():
    print("你想了解哪个 \033[1;30;47mBNF 语法符号\033[0m 的用途:")
    for index, option in enumerate(nota_list):
        print(f"{index+1}. {option}")
    choice = input("请输入选项的数字编号: ")

    # 检查用户输入是否有效
    if choice.isdigit() and int(choice) in range(1, len(nota_list)+1):
        selected_option = nota_list[int(choice)-1]
    else:
        print("无效的选项编号")
    return selected_option

search = msginput()

match (search):
    case ('::='):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“左侧是词法名称，右侧为词法规则的定义”\n'
              '例：\033[1;30;47mexponent ::= "a"..."z"\033[0m  意思为词法exponent是由单个小写a到z字母组成.')
    case ('|'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“或者的意思”\n'
              '例：\033[1;30;47mexponent ::= "a"|"z"\033[0m  意思为词法exponent只能是a或者z.')
    case ('*'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“对前一项重复0次或更多次”\n'
              '例：\033[1;30;47mexponent ::= （"a"..."z"）*\033[0m  意思为词法exponent是由0个（为空）或多个小写a到z字母组成.')
    case ('+'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“对前一项重复1次或更多次”\n'
              '例：\033[1;30;47mexponent ::= （"a"..."z"）+\033[0m  意思为词法exponent是由1个（不为空）或多个小写a到z字母组成.')
    case ('[...]'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“此项可选”\n'
              '例：\033[1;30;47mexponent ::= "test"["a"|"z"]\033[0m  意思为词法exponent可以是testa也可以是testz也可以是test.')
    case ('(...)'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“分组”\n'
              '例：\033[1;30;47mexponent ::= "test"（"a"|"z"）\033[0m  意思为词法exponent可以是testa也可以是testz，但不能是test.')
    case ('<...>'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“括起来的内容是对于所定义符号的非正式描述”\n'
              '例：\033[1;30;47mexponent ::= <This is a description，You can use any source character>\033[0m  意思为词法exponent要满足这里的描述.')
    case ('\"...\"'):
        print(f'\033[4;34;46m{search}解释:\033[0m 表示“引号中的字符序列本身，并非指代其它字”\n'
              '例：\033[1;30;47mexponent ::= test"()" \033[0m  意思为词法exponent先使用test词法，后面需要接上括号。\n'
              '如果test词法定义为由单个小写a到z字母组成,则当前exponent词法可以为 a()、b()...z()')
