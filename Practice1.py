Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_float=3.14
my_float
3.14

type(my_float)
<class 'float'>

type(my_int)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(my_int)
NameError: name 'my_int' is not defined
type(1)
<class 'int'>
1+2
3

my_int=1
type(my_int)
<class 'int'>
type(1)
<class 'int'>
my_int*100
100
my_int+3
4

my_j=1
my_j+1
2

Students = ['황동욱', '이병용', '이희녕', '전수현']
Students
['황동욱', '이병용', '이희녕', '전수현']
for std in students:
    print(std)

    
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    for std in students:
NameError: name 'students' is not defined. Did you mean: 'Students'?
for std in Students:
    print(std)

    
황동욱
이병용
이희녕
전수현
import random
print(random.choice(Students))
황동욱
print(random.choice(Students))
전수현
print(random.choice(Students))
이희녕
print(random.choice(Students))
전수현
Students.append('호돌이')
Students
['황동욱', '이병용', '이희녕', '전수현', '호돌이']
Stuednets.append('수돌이')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Stuednets.append('수돌이')
NameError: name 'Stuednets' is not defined. Did you mean: 'Students'?
Students.append('수돌이')
Students
['황동욱', '이병용', '이희녕', '전수현', '호돌이', '수돌이']
Students[6]= '호도리'
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    Students[6]= '호도리'
IndexError: list assignment index out of range
Students[5]='딸기'
Students
['황동욱', '이병용', '이희녕', '전수현', '호돌이', '딸기']
my_tuple=('요거트','이에스','레이')
my_tuple
('요거트', '이에스', '레이')
my_tuple[0]=
SyntaxError: invalid syntax
my_tuple[0]='딸기'
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    my_tuple[0]='딸기'
TypeError: 'tuple' object does not support item assignment
TypeError: 'tuple' object does not support item assignment
SyntaxError: invalid syntax

my_dict={'수현':'남', '소진':'여'}
my-dict['수현']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    my-dict['수현']
NameError: name 'my' is not defined
my_dict['수현']
'남'
my_dict['수현']='한국사람'
my_dict['수현']
'한국사람'


my_int=1
type(my_int)
<class 'int'>
float(my_int)
1.0
int(my_int)
1
my_int=1.5
type(my_int)
<class 'float'>
float(my_int)
1.5
int(my_int)
1
str(my_int)
'1.5'
type(str(my_int))
<class 'str'>


my_str="coding"
my_str
'coding'
list(my_str)
['c', 'o', 'd', 'i', 'n', 'g']
dictionary(my_str)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dictionary(my_str)
NameError: name 'dictionary' is not defined
NameError: name 'dictionary' is not defined
SyntaxError: invalid syntax


print('Hellow World!')
Hellow World!
print("Hello World!') #설명, 안녕을 표시합니다
      
SyntaxError: unterminated string literal (detected at line 1)
print('Hello World!') #설명, 안녕을 표시합니다
      
Hello World!


print(2 + 3) # 계산 결과를 설명합니다
      
5
5
      
5

my_str = "김씨가족"
      
print(my_str)
      
김씨가족

type(my_str)
      
<class 'str'>
my_str = '전씨가족'
      
print(my_str)
      
전씨가족
class(my_str)
SyntaxError: invalid syntax
type(my_str)
<class 'str'>

my_str = """전수현
히녕
동욱
"""
my_str
'전수현\n히녕\n동욱\n'
'전수현\n히녕\n동욱\n' # n은 줄바꿈을 나타냄
'전수현\n히녕\n동욱\n'
'전수현\n히녕\n동욱\n'
'전수현\n히녕\n동욱\n'

my_str = 'My name is %s' % 'Young Choi'

my_str
'My name is Young Choi'

'%d %d' % (1,2)
'1 2'

'%f' % 3.14
'3.140000'
'3.140000'
'3.140000'


'My name is []'.format('조희진')
'My name is []'

'My name is %s' % '조희진'
'My name is 조희진'
'My name is {}'.format('조희진')
'My name is 조희진'

'{}x{} = {}'.format(2,3,2*3)
'2x3 = 6'
'2x3 = 6'
'2x3 = 6'
'{} x {} = {}' .format(2, 3, 2*3)
'2 x 3 = 6'
'2 x 3 = 6'
'2 x 3 = 6'

'{1} x {0} = {2}' .format(2, 3, 2*3)
'3 x 2 = 6'


my_name = "김왼손의 왼손코딩"


my_name[3]
'의'
my_name[5]
'왼'
my_name[8]
'딩'
my_name[4]
' '
