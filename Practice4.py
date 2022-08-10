Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
range(3)
range(0, 3)
type(range(3))
<class 'range'>


for n in [0,,1,2]:
    
SyntaxError: invalid syntax
for n in [0,1,2]:
    print(n)

    
0
1
2

for n in range(0,3):
    print(n)

    
0
1
2


for i in range(1,10):
    print('[]x[]=[]'.format(2,i,2*i))

    
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]
[]x[]=[]

for j in range(2,10):
    for i in range(1,10):
        pring('[]x[]=[]'.format(j,i,j*i))

        
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    pring('[]x[]=[]'.format(j,i,j*i))
NameError: name 'pring' is not defined. Did you mean: 'print'?

for i in range(1,10):
    print('{}x{}={}'.format(2,i,2*i))

    
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18

for j in range(2,10):
    for i in range(1,10):
        print('{}x{}={}'.format(j,i,j*i))

        
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18
3x1=3
3x2=6
3x3=9
3x4=12
3x5=15
3x6=18
3x7=21
3x8=24
3x9=27
4x1=4
4x2=8
4x3=12
4x4=16
4x5=20
4x6=24
4x7=28
4x8=32
4x9=36
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
6x1=6
6x2=12
6x3=18
6x4=24
6x5=30
6x6=36
6x7=42
6x8=48
6x9=54
7x1=7
7x2=14
7x3=21
7x4=28
7x5=35
7x6=42
7x7=49
7x8=56
7x9=63
8x1=8
8x2=16
8x3=24
8x4=32
8x5=40
8x6=48
8x7=56
8x8=64
8x9=72
9x1=9
9x2=18
9x3=27
9x4=36
9x5=45
9x6=54
9x7=63
9x8=72
9x9=81
9x9=81
SyntaxError: invalid decimal literal

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number=[]

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

        
Traceback (most recent call last):
  File "<pyshell#39>", line 3, in <module>
    odd_numbers.append(number)
NameError: name 'odd_numbers' is not defined. Did you mean: 'odd_number'?
print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]














count = 0


cpimt
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    cpimt
NameError: name 'cpimt' is not defined
count
0


count = 1


count
1
count = count + 1

count
2
count = count + 1
count
3

count += 1
count
4
4
4


time_list = ["1","2","3","4"]
list(map(int, time_list))
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
timelist(map(int,time_list))
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    timelist(map(int,time_list))
NameError: name 'timelist' is not defined. Did you mean: 'time_list'?
timelist
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    timelist
NameError: name 'timelist' is not defined. Did you mean: 'time_list'?
time_list(map(int,time_list))
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    time_list(map(int,time_list))
TypeError: 'list' object is not callable
time_list
['1', '2', '3', '4']
list(map(int,time_list))
[1, 2, 3, 4]
list
<class 'list'>


a = [1,2,3,]
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

list(map(lambda x,y:x+y, a,b)

    print(c)
     
SyntaxError: '(' was never closed
SyntaxError: '(' was never closed
     
SyntaxError: invalid syntax

a
     
[1, 2, 3]
map(labda x,y:x+y, a,b)
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
list(map(labda x,y:x+y, a,b))
     
SyntaxError: invalid syntax. Perhaps you forgot a comma?
map(lambda x,y:x+y, a,b)
     
<map object at 0x000001B405DD16F0>
list(map(lambda x,y:x+y, a,b))
     
[5, 7, 9]
c=list(map(lambda x,y:x+y, a,b))
     
list
     
<class 'list'>
print(c)
     
[5, 7, 9]



[5, 7, 9]
     
[5, 7, 9]

list(map(lambda x,y:x+y, a,b))
     
[5, 7, 9]
[5, 7, 9]
     
[5, 7, 9]
c
     
[5, 7, 9]
c=list(map(lambda x,y:x+y, a,b))
     
print(c)
     
[5, 7, 9]


a=[1,2,3]
     
b=[4,5,6]
     
c=[7,8,9]
     
map(lambda x,y:x+y, a,b)
     
<map object at 0x000001B405DD2320>
list(map(lambda x,y:x+y, a,b))
     
[5, 7, 9]
c=list(map(lambda x,y:x+y, a,b))
     
print(c)
     
[5, 7, 9]


a=[1,2,3]
     
b=[4,5,6]
     
c=[5,7,9]
     
map(lambda x,y:x+y, a,b)
     
<map object at 0x000001B405DD2320>
list(map(lambda x,y:x+y, a,b))
     
[5, 7, 9]
c=list(map(lambda x,y:x+y, a,b))
     
print(c)
     
[5, 7, 9]
     
SyntaxError: multiple statements found while compiling a single statement


3 ** 2
     
9
4 ** 2
     
16
4 **3
     
64
7//2
     
3
7/3
     
2.3333333333333335


numbers = [1,2,3,4,5,6,7]
     
for in number in numbers
     
SyntaxError: invalid syntax
for number in numbers
     
SyntaxError: expected ':'
SyntaxError: expected ':'
     
SyntaxError: invalid syntax
for number in numbers:
     print(number)

     
1
2
3
4
5
6
7


if 1 % 2 == 1:
     print("홀수")

     
홀수
if 2 % 2 == 0:
     print("짝수1")

     
짝수1



for number in numbers:
     if number % 2 == 1:
     print("홀수!")
     
SyntaxError: expected an indented block after 'if' statement on line 2


for number in numbers:
     if number % 2 == 1:
     print("홀수)
           
SyntaxError: unterminated string literal (detected at line 3)

for number in numbers:
     if number % 2 == 1:
     print("홀수")
           
SyntaxError: expected an indented block after 'if' statement on line 2
for number in numbers:
     if number % 2 == 1:
     print("홀수")
           
SyntaxError: expected an indented block after 'if' statement on line 2

for number in numbers:
           if number % 2 == 1:
               print("홀수!")

           
홀수!
홀수!
홀수!
홀수!
for number in numbers:
           if number % 2 == 1:
               print("홀수!")
           else:
               print("짝수!")

               
홀수!
짝수!
홀수!
짝수!
홀수!
짝수!
홀수!

for number in numbers:
    if number % 2 == 1:
        print("홀")
        else:
            
SyntaxError: invalid syntax

for number in numbers:
        if number % 2 == 1:
            print('홀')
            else:
                
SyntaxError: invalid syntax
for number in numbers:
        if number % 2 == 1:
            print('홀')
            else:
                
SyntaxError: invalid syntax



def cls():
    print('\n'*100)

    

def cls():
    print('\n'*100)
cls()
SyntaxError: invalid syntax
cls
<function cls at 0x000001B405E03D00>
cls()

def cls():
    print('\n'*2)

    
cls()



def cls():
    print('\n'*2)

    


1 < 2
True
2 < 1
False
1 != 2
True
True
True


height > 140 and age > 10
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    height > 140 and age > 10
NameError: name 'height' is not defined
height = 120
age = 8
height > 140 and age > 10
False

h=190
age=9

h>140 and age . 10
SyntaxError: invalid syntax
h>140 and age>10
False
h=150
age=32

h>140 and age>10
True


input_name= '김왼손'
if input_name=='김왼손':
    print('만나서 반가워요,', input_name)

    
만나서 반가워요, 김왼손


if hame == '김왼손':
    print('당신이 김왼손이군요!')
elif name == '호박':
    print('당신이 호박이군요!')
elif name == 'Meta':
    print('당신이 Meta군요!')
else:
    print('당신은!?')

    
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    if hame == '김왼손':
NameError: name 'hame' is not defined
if name == '김왼손':
    print('당신이 김왼손이군요!')
elif name == '호박':
    print('당신이 호박이군요!')
elif name == 'Meta':
    print('당신이 Meta군요!')
else:
    print('당신은!?')

    
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    if name == '김왼손':
NameError: name 'name' is not defined
if name == '김왼손':
    print('당신이 김왼손이군요!')
elif name == '호박':
    print('당신이 호박이군요!')
elif name == 'Meta':
    print('당신이 Meta군요!')
else:
    print('당신은!?')

    
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    if name == '김왼손':
NameError: name 'name' is not defined
if name == '김왼손':
    print('당신이 김왼손이군요!')
elif name == '호박':
    print('당신이 호박이군요!')
elif name == 'Meta':
    print('당신이 Meta군요!')
else:
    print('당신은!?')

    
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    if name == '김왼손':
NameError: name 'name' is not defined
NameError: name 'name' is not defined
SyntaxError: invalid syntax

count = 0
 while count <3:
     
SyntaxError: unexpected indent
while count <3:
    print('횟수
          
SyntaxError: unterminated string literal (detected at line 2)

while count <3:
    print('횟수:', 0)
    count += 1

    
횟수: 0
횟수: 0
횟수: 0
횟수: 0


count = 0

while count < 10:
    count += 1
    if count < 4:
        coutinue
    print('횟수:', count)
    if count == 8:
        break

    
Traceback (most recent call last):
  File "<pyshell#271>", line 4, in <module>
    coutinue
NameError: name 'coutinue' is not defined


my_dict[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    my_dict[0] = 'a'
NameError: name 'my_dict' is not defined
my-dict
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    my-dict
NameError: name 'my' is not defined
NameError: name 'my' is not defined
SyntaxError: invalid syntax

my_dict
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    my_dict
NameError: name 'my_dict' is not defined
