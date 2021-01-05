#!/usr/bin/python
import re


def main():
    # <editor-fold desc='匹配任意字符关键字'>
    pattern = re.compile(r'.a.\.xls')
    result1 = pattern.findall('sales.xls'
                              'sales1.xls'
                              'orders3.xls'
                              'sales2.xls'
                              'sales3.xls'
                              'apac1.xls'
                              'europe2.xls'
                              'na1.xls'
                              'na2.xls'
                              'sa2.xls'
                              'ca1.xls')

    print(result1)  # ['na1.xls', 'na2.xls', 'sa2.xls', 'ca1.xls']
    # </editor-fold>

    # <editor-fold desc='匹配一组字符关键字[]'>
    pattern = re.compile(r'[ns]a.\.xls')
    result1 = pattern.findall('sales.xls'
                              'sales1.xls'
                              'orders3.xls'
                              'sales2.xls'
                              'sales3.xls'
                              'apac1.xls'
                              'europe2.xls'
                              'na1.xls'
                              'na2.xls'
                              'sa2.xls'
                              'ca1.xls')

    print(result1)  # ['na1.xls', 'na2.xls', 'sa2.xls']
    # </editor-fold>

    # <editor-fold desc='大小写'>
    pattern = re.compile(r'[Rr]eg[Ee]x')

    result1 = pattern.findall('RegEx or regex or REGEX.')

    print(result1)  # ['RegEx', 'regex']
    # </editor-fold>

    # <editor-fold desc='集合区间'>
    pattern = re.compile(r'[ns]a[0123456789]\.xls')
    pattern = re.compile(r'[ns]a[0-9]\.xls')

    result1 = pattern.findall('sales.xls'
                              'sales1.xls'
                              'orders3.xls'
                              'sales2.xls'
                              'sales3.xls'
                              'apac1.xls'
                              'europe2.xls'
                              'sam.xls'
                              'na1.xls'
                              'na2.xls'
                              'sa1.xls'
                              'ca1.xls')

    print(result1)  # ['na1.xls', 'na2.xls', 'sa1.xls']
    # </editor-fold>

    # <editor-fold desc='读取rgb值'>
    # [A-Z] 匹配A到Z所有大写字母
    # [a-z] 匹配a到z所有小写字母
    # [A-F] 匹配A到F所有大写字母
    # [A-z] 匹配从ASCII字符A到ASCII字符z的所有字母
    # [A-Za-z0-9] 匹配任何一个字母无论大小写或数字

    pattern = re.compile(r'#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]')

    result1 = pattern.findall('body { background-color: #fefdb8; }'
                              'h1   { background-color: #0000ff; }'
                              'div  { background-color: #d0f4e6; }'
                              'span { background-color: #f08970; }')

    print(result1)  # ['#fefdb8', '#0000ff', '#d0f4e6', '#f08970']
    # </editor-fold>

    # <editor-fold desc='排除关键字^'>
    pattern = re.compile(r'[ns]a[^0-9]\.xls')

    result1 = pattern.findall('sales.xls'
                              'sales1.xls'
                              'orders3.xls'
                              'sales2.xls'
                              'sales3.xls'
                              'apac1.xls'
                              'europe2.xls'
                              'sam.xls'
                              'na1.xls'
                              'na2.xls'
                              'sa1.xls'
                              'ca1.xls')

    print(result1)  # ['sam.xls']
    # </editor-fold>

    # <editor-fold desc='匹配空白字符'>
    # 关键字
    # [\b] 回退(并删除)一个字符(Backspace)
    # \f 换页符
    # \n 换行符
    # \r 回车符
    # \t 制表符
    # \v 垂直制表符
    pattern = re.compile(r'\r\n\r\n')

    result1 = pattern.findall('101'
                              '202'
                              ""
                              '303')

    print(result1)  # 匹配空行
    # </editor-fold>

    # <editor-fold desc='匹配特定字符串类型'>
    # 匹配数字,非数字
    # \d 任何一个数字字符 等价 [0-9]
    # \D 任何一个非数字字符 等价 [^0-9]

    # 匹配字母数字,非字母数字
    # \w 任何一个字母数字字符(大小写均可)或下划线字符(等价于[a-zA-Z0-9_])
    # \W 任何一个非字母数字字符或非下划线字符(等价于[^a-zA-Z0-9_])
    pattern = re.compile(r'\w\d\w\d\w\d')

    result1 = pattern.findall('11213\r\n'
                              'A1C2E3\r\n'
                              '48075\r\n'
                              '48237\r\n'
                              'M1B4F2\r\n'
                              '90046\r\n'
                              'H1H2H2\r\n')

    print(result1)  # ['A1C2E3', 'M1B4F2', 'H1H2H2']
    # </editor-fold>

    # <editor-fold desc='匹配空白字符,非空白字符'>
    # \s 任何一个空白字符 等价 [\f\n\r\t\v]
    # \S 任何一个非空白字符 等价 [^\f\n\r\t\v]

    # </editor-fold>

    # <editor-fold desc='匹配十六进制或八进制数值'>
    # \x 十六进制
    # ex: \x0A 对应ASCII10 等价于 \n

    # \0 八进制
    # ex: \011 对应ASCII9 等价于\t

    # </editor-fold>

    # <editor-fold desc='POSIX, 不过py不支持'>

    # [:alnum:] 任何一个字母或数字(等价于[a-zA-Z0-9])
    # [:alpha:] 任何一个字母(等价于[a-zA-Z])
    # [:blank:] 空格或制表符(等价于[\t ])
    # [:cntrl:] ASCII控制字符(ASCII 0到31, 再加上ASCII 127)
    # [:digit:] 任何一个数字(等价于[0-9])
    # [:graph:] 和[:print:]一样,但不包括空格
    # [:lower:] 任何一个小写字母(等价于[a-z])
    # [:print:] 任何一个可打印字符
    # [:punct:] 既不属于[:alnum:], 也不属于[:cntrl:]的任何一个字符
    # [:space:] 任何一个空白字符,包括空格(等价于[\f\n\r\t\v\ ])
    # [:upper:] 任何一个大写字母(等价于[A-Z])
    # [:xdigit:] 任何一个十六进制数字(等价于[a-fA-F0-9])

    # </editor-fold>

    # <editor-fold desc='匹配一个或多个字符'>
    # +号匹配 1~N个字符
    # []内\.和.等价
    pattern = re.compile(r'[\w\.]+@[\w.]+\.\w+')

    result1 = pattern.findall('ben@forta.com\n'
                              'ben.forta@forta.com\n'
                              'support@forta.com\n'
                              'ben@urgent.forta.com\n'
                              'spam@forta.com\n')

    # ['ben@forta.com', 'ben.forta@forta.com', 'support@forta.com', 'ben@urgent.forta.com', 'spam@forta.com']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='匹配零个或多个字符'>
    # *号匹配 0~N个字符
    # []内\.和.等价
    pattern = re.compile(r'\w+[\w.]*@[\w.]+\.\w+')

    result1 = pattern.findall('.ben@forta.com\n'
                              '.ben.forta@forta.com\n')

    # ['ben@forta.com', 'ben.forta@forta.com']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='匹配零个或一个字符'>
    # ?号匹配 0~1个字符(最多一次)
    pattern = re.compile(r'https?:\/\/[\w.\/]+')

    result1 = pattern.findall('http://www.forta.com/ test https://www.forta.com/')

    # ['http://www.forta.com/', 'https://www.forta.com/']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='匹配重复次数'>
    # {次数}
    pattern = re.compile(r'#[0-9A-Fa-f]{6}')

    result1 = pattern.findall('body { background-color: #fefdb8; }'
                              'h1   { background-color: #0000ff; }'
                              'div  { background-color: #d0f4e6; }'
                              'span { background-color: #f08970; }')

    print(result1)  # ['#fefdb8', '#0000ff', '#d0f4e6', '#f08970']

    # </editor-fold>

    # <editor-fold desc='区间范围'>
    # {最小, 最大} ex:{2, 4} 最少重复2次, 最多重复4次
    # {0,1} 等价于 ?
    pattern = re.compile(r'\d{1,2}[-\/]\d{1,2}[-\/]\d{2,4}')

    result1 = pattern.findall('4/8/17\n'
                              '10-6-2018\n'
                              '2/2/2\n'
                              '01-01-01\n')

    # ['4/8/17', '10-6-2018', '01-01-01']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='至少重复多少次'>
    # {至少次数,} 重复 至少次数 或更多
    # {1,} 等价于 +
    # 找出金额大于100的
    pattern = re.compile(r'\d+: \$\d{3,}\.\d{2}')

    result1 = pattern.findall('1001: $496.80\n'
                              '1002: $1290.69\n'
                              '1003: $26.43\n'
                              '1004: $613.42\n'
                              '1005: $7.61\n'
                              '1006: $414.90\n'
                              '1007: $25.00\n')

    # ['1001: $496.80', '1002: $1290.69', '1004: $613.42', '1006: $414.90']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='防止过度匹配'>
    # * + {} 都是greedy型
    # 后面添加?就是 懒惰版本

    # ['<b>AK</b> and <b>HI</b>']
    pattern = re.compile(r'<[Bb]>.*<\/[Bb]>')
    # ['<b>AK</b>', '<b>HI</b>']
    pattern = re.compile(r'<[Bb]>.*?<\/[Bb]>')

    result1 = pattern.findall('This offer is not available to customer living in <b>AK</b> and <b>HI</b>')

    print(result1)

    # </editor-fold>

    # <editor-fold desc='单词边界'>
    # \b 匹配单词边界

    pattern = re.compile(r'\bcat\b')

    result1 = pattern.findall('The cat scattered his food all over the room.')

    # ['cat']
    print(result1)

    pattern = re.compile(r'\bcap')

    result1 = pattern.findall('captain cap cape recap')

    # ['cap', 'cap', 'cap']
    print(result1)

    pattern = re.compile(r'cap\b')

    result1 = pattern.findall('captain cap cape recap')

    # ['cap', 'cap']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='非单词边界'>
    # \B 匹配非单词边界

    pattern = re.compile(r'\B-\B')

    result1 = pattern.findall('color - coded nine-digit')

    # ['-']
    print(result1)
    # </editor-fold>

    # <editor-fold desc='字符串边界'>
    # ^ 字符串开头 ([]内^才是取反)
    # $ 字符串结尾

    # 如果xml之前有其他字符或者其他行, 就会匹配失败
    # ['<?xml version='1.0' encoding='utf-8'?>']
    pattern = re.compile(r'^\s*<\?xml.*\?>')
    # 匹配尾巴的
    # ['<manifest>']
    pattern = re.compile(r'<manifest>$')

    result1 = pattern.findall('<?xml version=\'1.0\' encoding=\'utf-8\'?><manifest><manifest>')

    print(result1)

    # </editor-fold>

    # <editor-fold desc='多行模式'>
    # (?m) 打开多行模式, 打开后会把换行符视为字符串分隔符
    # 这样就可以用^$匹配字符串换行后的起始和结束位置

    pattern = re.compile(r'(?m)^\s*\/\/.*$')

    result1 = pattern.findall('// 注释1 \n'
                              'code123\n'
                              '// 注释2\n'
                              'code123 \n'
                              '//注释123 注释456')

    # ['// 注释1 ', '// 注释2', '//注释123 注释456']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='子表达式'>
    # () 关键字

    # 无法正确匹配, 只能匹配 &nbsp;;;
    pattern = re.compile(r'&nbsp;{2,}')

    pattern = re.compile(r'(&nbsp;){2,}')

    result1 = pattern.findall('Test&nbsp;&nbsp;&nbsp;&nbsp;Test')

    # ['// 注释1 ', '// 注释2', '//注释123 注释456']
    print(result1)

    # ['12.123.12.200']
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    # [('12.123.14.200', '14.')]
    pattern = re.compile(r'((\d{1,3}\.){3}\d{1,3})')

    # ['14.']
    pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

    # ['12.123.14.200']
    pattern = re.compile(r'(?:\d{1,3}\.){3}\d{1,3}')

    result1 = pattern.findall('[12.123.14.200]')

    print(result1)

    # <re.Match object; span=(1, 14), match='12.123.14.200'>
    print(re.search(pattern, '[12.123.14.200]'))

    # [('1967', '19')]
    pattern = re.compile(r'((19|20)\d{2})')

    result1 = pattern.findall('1967-08-17')

    print(result1)

    # </editor-fold>

    # <editor-fold desc='补充上面子表达式中的()和findall在py下的注意'>

    s = 'adfad asdfasdf asdfas asdfawef asd adsfas '

    reObj1 = re.compile(r'((\w+)\s+\w+)')

    # [('adfad asdfasdf', 'adfad'), ('asdfas asdfawef', 'asdfas'), ('asd adsfas', 'asd')]
    print(reObj1.findall(s))

    reObj2 = re.compile(r'(\w+)\s+\w+')

    # ['adfad', 'asdfas', 'asd']
    print(reObj2.findall(s))

    reObj3 = re.compile(r'\w+\s+\w+')

    # ['adfad asdfasdf', 'asdfas asdfawef', 'asd adsfas']
    print(reObj3.findall(s))

    # 按以上代码例子讲解:
    #
    # findall函数返回的总是正则表达式在字符串中所有匹配结果的列表
    # 此处主要讨论列表中'结果'的展现方式
    # 即findall中返回列表中每个元素包含的信息
    # 1.当给出的正则表达式中带有多个括号时
    #   列表的元素为多个字符串组成的tuple
    #   tuple中字符串个数与括号对数相同
    #   字符串内容与每个括号内的正则表达式相对应
    #   并且排放顺序是按括号出现的顺序。
    #
    # 2.当给出的正则表达式中带有一个括号时
    #   列表的元素为字符串
    #   此字符串的内容与括号中的正则表达式相对应(不是整个正则表达式的匹配内容)
    #
    # 3.当给出的正则表达式中不带括号时
    #   列表的元素为字符串
    #   此字符串为整个正则表达式匹配的内容
    #
    # </editor-fold>

    # <editor-fold desc='匹配有效ip'>
    # 注意顺序
    pattern = re.compile(
        r'((((25[0-5])|(2[0-4]\d)|(1[0-9]\d)|(\d{1,2}))\.){3}((25[0-5])|(2[0-4]\d)|(1[0-9]\d)|(\d{1,2})))')

    result1 = pattern.findall('[12.159.46.200]')

    # [('12.159.46.200', '46.', '46', '', '', '159', '46', '200', '', '200', '', '')]
    print(result1)

    # 替换成更符合逻辑的写法会有问题
    # 从左往右匹配, 如果满足就会给出结果
    pattern = re.compile(
        r'((((\d{1,2})|(1[0-9]\d)|(2[0-4]\d)|(25[0-5])|)\.){3}((\d{1,2})|(1[0-9]\d)|(2[0-4]\d)|(25[0-5])|))')

    result1 = pattern.findall('[12.159.46.200]')

    # [('12.159.46.20', '46.', '46', '46', '159', '', '', '20', '20', '', '', '')]
    print(result1)

    # </editor-fold>

    # <editor-fold desc='反向引用或回溯引用(backreference)'>
    # ()代表一个子表达式
    # 之后使用\n(1开始)代表引用先前的第n个表达式
    # 部分正则实现中\0可以代表整个表达式
    # 注意多个()的情况

    # ['of', 'and', 'are']
    pattern = re.compile(r'[ ](\w+)[ ]\1')

    # [(' of ', 'of'), (' and ', 'and'), (' are ', 'are')]
    pattern = re.compile(r'([ ](\w+)[ ])\2')

    # [(' of of', 'of'), (' and and', 'and'), (' are are', 'are')]
    pattern = re.compile(r'([ ](\w+)[ ]\2)')

    result1 = pattern.findall('xx of of xxx and and xxx are are.')

    print(result1)

    pattern = re.compile(r'(<[hH]([1-6])>.*?<\/[hH]\2>)')

    result1 = pattern.findall('<body>\n'
                              '<h1>Test1</h1>\n'
                              'Test2\n'
                              '<h2>Test3</h2>\n'
                              'Test4\n'
                              '<h3>Test5</h3>\n'
                              'Test6<br/>\n'
                              '</body>\n')

    # [('<h1>Test1</h1>', '1'), ('<h2>Test3</h2>', '2'), ('<h3>Test5</h3>', '3')]
    print(result1)

    # </editor-fold>

    # <editor-fold desc='替换操作'>
    # 替换的串中和backreference一样使用\n替换子表达式

    pattern = re.compile(r'([\w\.]+@[\w.]+\.\w+)')

    s = 'ben@forta.com\n' + \
        'abcdefg\n' + \
        'ben.forta@forta.com\n' + \
        'abcdefg'

    result1 = pattern.findall(s)
    replstr = r'<a href="mailto:\1">\1</a>'

    # ['ben@forta.com', 'ben.forta@forta.com']
    print(result1)

    print('---------------')
    print(s)
    print('----↓↓↓↓↓↓↓----')
    print(pattern.sub(replstr, s))
    print('---------------')

    pattern = re.compile(r'(\d{3})(-)(\d{3})(-)(\d{4})')

    s = '333-157-1507\n' + \
        '123-403-1570\n' + \
        '111-578-8456\n' + \
        '234-237-4856'

    result1 = pattern.findall(s)
    replstr = r'(\1) \3-\5'

    # [('333', '-', '157', '-', '1507'),
    # ('123', '-', '403', '-', '1570'),
    # ('111', '-', '578', '-', '8456'),
    # ('234', '-', '237', '-', '4856')]
    print(result1)

    print('---------------')
    print(s)
    print('----↓↓↓↓↓↓↓----')
    print(pattern.sub(replstr, s))
    print('---------------')

    # </editor-fold>

    # <editor-fold desc='大小写转换'>
    # 正则配合backreference
    # \E \L,\U的结束符
    # \l 将下一个字符转换成小写
    # \L 将\L至\E之间的字符都转换成小写
    # \u 将下一个字符转换成大写
    # \U 将\U至\E之间的字符都转换成小写
    # py的话需要像下面这样处理
    # 以上关键字会报错

    pattern = re.compile(r'([\w\.]+@[\w.]+\.\w+)')

    s = 'ben@forta.com\n' + \
        'abcdefg\n' + \
        'ben.forta@forta.com\n' + \
        'abcdefg'

    result1 = pattern.findall(s)

    # 'Test[{\U\1\E}]
    def callback(word): return 'Test[{}]'.format(word.group(1).upper())

    # ['ben@forta.com', 'ben.forta@forta.com']
    print(result1)

    print('---------------')
    print(s)
    print('----↓↓↓↓↓↓↓----')
    print(pattern.sub(callback, s))
    print('---------------')

    # </editor-fold>

    # <editor-fold desc='向前查找'>
    # 查看已匹配文本之后的内容
    # (?=)

    # ['https:', 'https:']
    pattern = re.compile(r'.+:')

    # ['https', 'https']
    pattern = re.compile(r'.+(?=:)')

    result1 = pattern.findall('https://www.bilibili.com/\n'
                              'https://www.baidu.com/\n')

    print(result1)

    # </editor-fold>

    # <editor-fold desc='向后查找'>
    # (?<=)

    pattern = re.compile(r'(?<=\$)[\d.]+')

    result1 = pattern.findall('1.24\n'
                              '4685.6845\n'
                              '$ 4685.6845\n'
                              '$15978685.45\n'
                              '$12346785852.54$\n'
                              '4568.96 $64987.69\n')

    # ['15978685.45', '12346785852.54', '64987.69']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='结合向前向后'>

    pattern = re.compile(r'(?<=\<[tT][iI][tT][lL][eE]\>).*(?=\<\/[tT][iI][tT][lL][eE]\>)')

    result1 = pattern.findall('<head>\n'
                              '<title>Test 123 learning regex.</title>\n'
                              '</head>')

    # ['Test 123 learning regex.']
    print(result1)

    # </editor-fold>

    # <editor-fold desc='否定式环视'>
    # = 替换为 !
    # ?=  --> ?!
    # ?<= --> ?<!

    pattern = re.compile(r'\b(?<!\$)\d+\b')

    result1 = pattern.findall('1 24\n'
                              '$30\n'
                              '200\n'
                              '$ 300123\n'
                              '$15945\n'
                              '$123454$\n'
                              '456896 $6498769\n')

    # ['1', '24', '466845', '4686845', '456896']
    print(result1)

    # </editor-fold>


if __name__ == '__main__':
    main()
    pass
