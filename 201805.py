#! usr/bin/python3
print("Hello world")
x = 666
print("x * 3 =", x * 3)
print("\n 17/6  is ", 17/6)
print("\n 17//6 is ", 17//6)
print("\n 17 % 6 is" , 17 % 6 )

G = 6.67 * 10 ** (-11)
M = 5.98 * 10 ** 24
R = 6380 * 10 ** 3
g = G*M/(R**2) #g=GMR2

x = 114514
if x%3 ==0:
    print(x, "能被3整除")
else:
    print(x, "不能被3整除")

'''
判断是否一个数为质数：
仅能被1和自己本身整除
'''
xx = 3
if xx > 1:
    for i in range(2,xx):
        if xx%i == 0:
            print(xx, " is not a prime number")
            print(i, "is prime factor")
            break
        else:
            print(xx, "is a prime number")

else:
    print(xx, "is not a prime number")

#list
lst = [2,3,4]
lst[0]
lst[-1]
lst[2] = "foo"
print(lst)
lst.append("okla")
lst.pop()

#斐波那契数列
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(4))

###二分查找
def binary_search(lst, item):

    # 下界索引
    low = 0
    # 上界索引
    high = len(lst) - 1

    while low <= high:
        # 中值
        mid = int((low + high) / 2)
        # 猜测结果
        guess = lst[mid]

        # 猜中
        if guess == item:
            return mid
        # 偏大
        elif guess > item:
            high = mid - 1
        # 偏小
        else:
            low = mid + 1

    # 查找不到
    return None

print(binary_search([0,1,2,3,5,8,13], 8))

#python 内置
lst = [3,1,4,1,5,9,2,6]
lst.index(9)    # 5
lst.count(1)    # 1

#python内置查找关键字
primes = [2, 3, 5, 7, 11, 13, 17, 19]
print("9 In primes ->", 9 in primes)
print("9 Not in primes -> ", 9 not in primes)

#选择排序
def find_smallest(lst):
    # 先假设列表第0元素为最小
    smallest = lst[0]
    smallest_index = 0

    for i in range(1, len(lst)):
        # 如果比当前的“最小”还小
        if lst[i] < smallest:
            # 替换当前的“最小”
            smallest = lst[i]
            smallest_index = i
    # 返回最小值的索引
    return smallest_index


def selection_sort(lst):

    new_lst = []
    for _ in range(len(lst)):
        smallest = find_smallest(lst)
        new_lst.append(lst.pop(smallest))
    return new_lst

#阶层
def fact(n):
    if n > 1:
        return fact(n-1) * n
    elif n == 1:
        return n

#快速排序，递归
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        temp = lst[0]
        temp_upper = [i for i in lst[1:] if i > temp]
        temp_lower = [i for i in lst[1:] if i <= temp]
        return quicksort(temp_lower) + [temp] + quicksort(temp_upper)

print(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 8]))

#dictionary
hans = {"及时雨":"Songjiang",
        "玉麒麟": "卢俊义",
        "智多星": "吴用"
        }
print('"及时雨" in hans = ', "及时雨" in hans)
print('"宋江" in hans.values() =', "Songjiang" in hans.values())
for key in hans:
    print(key)

#pi,统计该列表中0-9十位数字分别出现了多少次
pi_lst = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']

pi_counts = {}
for key in pi_lst:

    if key in pi_counts:
        pi_counts[key] += 1

    else:
        pi_counts[key] = 1

#每个出现频次对应的数字, reverse
pi_lst = ['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5', '0', '2', '8', '8', '4', '1', '9', '7', '1', '6', '9', '3', '9', '9', '3', '7', '5', '1', '0', '5', '8', '2', '0', '9', '7', '4', '9', '4', '4', '5', '9', '2', '3', '0', '7', '8', '1', '6', '4', '0', '6', '2', '8', '6', '2', '0', '8', '9', '9', '8', '6', '2', '8', '0', '3', '4', '8', '2', '5', '3', '4', '2', '1', '1', '7', '0', '6', '7', '9']

pi_counts = {'3': 12, '1': 8, '4': 10, '5': 8, '9': 14, '2': 12, '6': 9, '8': 12, '7': 8, '0': 8}
inverse = {}

for value in pi_counts.values():
    inverse[value] = [key for key in pi_counts if pi_counts[key] == value]

###string, 修改string
yizhao_str = "传位十四阿哥"
    # 生成一个新的变量，暂时是空字符串（只有俩引号）
new_yizhao_str = ''
for i in yizhao_str:
    if i == "十":
        i = "于"
    else:
        i = i
    new_yizhao_str += i

###replace()
yizhao_str = "传位十四阿哥"
yizhao_str.replace("十", "于")

print(yizhao_str)
print(yizhao_str.replace("十", "于"))

###GNA-> RNA
def dna2rna(dna):
    rna = ""
# >>>> show me the code <<<<
    for i in dna:
        if i == "T":
            i = "U"
        rna += i
    return rna

###.lower, .upper()
"HHH".lower()
"AHsadfa".upper()

###count
"banana".count("a")

###caesar
def caesar_cipher(phrase, shift):
    input_phrase = phrase.lower()
    output_phrase = ''
    for i in input_phrase:
        output_phrase += chr(ord(i)+shift).upper()
    return output_phrase

### %格式化
print("%d岁，%s" % (24, "学生"))
print("%dage,%s" % (24,"Student"))
print("Pi的小数点前5位是%.5f" % 3.1415926535898)
print("他的生日是%d\\%02d\\%02d" % (1921, 7, 1))

# .format()格式化
print("\n{}岁，{}".format(24, "学生") )
print("Pi的小数点前5位是{:.5f}".format(3.1415926535898))
print("他的生日是{}\\{:02d}\\{:02d}".format(1921, 7, 1))

# 参数顺序
print("\n如果{1}追到{0}，我就和你嘿嘿嘿".format("你", "我"))

# 对齐
print("{:^16}".format("嘿嘿嘿"))
print("{:<16}".format("嘿嘿嘿"))
print("{:>16}".format("嘿嘿嘿"))

###string to list
phrase_str = "风 评 被 害"
phrase_lst = phrase_str.split(' ')

###去除空格
phrase = '    乖 乖 站 好    '
print('strip() -> ', phrase.strip())
print('lstrip() -> ', phrase.lstrip())
print('rstrip() -> ', phrase.rstrip())

###morse code
morse_decode = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
                '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
                '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '...---...': 'SOS'}
def decode_morse(input_phrase):
    input_phrase = input_phrase.split(' ')
    print(input_phrase)
    output_phrase = ''

    for i in input_phrase:
        if i == '':
            output_phrase += ' '
        else:
            output_phrase += morse_decode[i]
    return output_phrase.lstrip().rstrip()
print(decode_morse('      - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.      '))

###
def dna_strand(dna):
    # >>>> sheng wu da fa hao <<<<
    dna_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rna = ""
    for i in dna:
        if i in dna_dict:
            rna += dna_dict[i]
        else:
            rna += i
    return rna

###列表推导式
def sum_of_multiples(number):
    return sum(i for i in range(number) if i % 3 ==0 or i % 5 == 0)

###元音count
def letter_counts(input_str):
    # letter_counts('abcdefgABCDEFG') 应该返回 4
    return sum(1 for i in input_str if i in "aeiouAEIOU" )

###转16进制
def rgb_to_hex(r,g,b):
    # rgb_to_hex(255, 255, 255) 应该返回 'FFFFFF'
    # rgb_to_hex(0, 0, 0) 应该返回 '000000'
    return "{:02X}{:02X}{:02X}".format(r,g,b)

###dig_power
def dig_pow(n, p):
    # dig_pow(89, 1) 返回 1，因为 8¹ + 9² = 89，89 / 89 == 1
    # dig_pow(695, 2) 返回 2，因为 6² + 9³ + 5⁴= 1390，1390 / 695 == 2
    # dig_pow(46288, 3) 返回 51 因为 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688，2360688 / 46288 == 51
    # 如果不能整除，返回 -1
    a = sum([int(j) ** (p+i) for i, j in enumerate(str(n))])
    if a % n == 0:
        return a/n
    else:
        return -1

###输出最大数字
def biggest(n):
    n_sorted = sorted([int(i) for i in str(n)])
    big = sum(j*10**i for i,j in enumerate(n_sorted))
    return big

###roman
def num_to_roman(num):

    roman_num = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman_str = ''

    for key in sorted(roman_num,reverse=True):

        while num >= key:
            roman_str += roman_num[key]
            num -= key

    return roman_str

###圆括号单配对
def valid_parentheses(input_str):

    left = 0

    for i in input_str:

        if i == "(":
            left += 1

        if i == ")":
            left -= 1

        if left < 0:
            return False
            break

    return left == 0

###多个括号配对
def valid_braces(input_str):
    # valid_braces("())({}}{()][][") -> False
    # valid_braces("(({{[[]]}}))") -> True
    # >>>> show me the code <<<<
    left = ["(","{","["]
    right = {")":"(","}":"{","]":"["}
    stack = []
    try:
        for i in input_str:
            if i in left:
                stack.append(i)
            if i in right:
                if stack[-1] == right[i]:
                    stack.pop()
                else:
                    return False
                    break
    except IndexError:
        return False
    return stack == []

###优雅的搓出螺旋丸！
def snail(input_arr):
    '''
    [[1,2,3],
     [4,5,6],
      [7,8,9] --> [1,2,3,6,9,8,7,4,5]
    '''
    output_arr = []
    while input_arr:
        output_arr.extend(input_arr.pop(0))
        temp_arr = []
        for i in zip(*input_arr):
            temp_arr.append(list(i))
        input_arr = temp_arr[::-1]
    return output_arr

###numpy exercise
import numpy as np
a = np.arange(15).reshape(3,5)
a.shape

a.dtype.name

a.dim

type(a)
