Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
two_digit_number = input("Type a two digit number: ")
Type a two digit number: 35

first_digit=two_digit_number[0]
second_digit=two_digit_number[1]

print(first_digit)
3
print(second_digit)
5
result=first_digit+second_digit
print(type(first_digit))
<class 'str'>

result=int(first_digit)+int(second_digit)
print(result)
8

print(round(8/3))
3

print(round(2.666666,2))
2.67

print(type(8//3))
<class 'int'>
print(type(8/3))
<class 'float'>

score = 0
score += 1
print(score)
1
print(score)
1

print("your score is" + str(score))
your score is1

score = 0
height = 1.8
isWinning = Ture
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    isWinning = Ture
NameError: name 'Ture' is not defined
isWinning = True

print(f"your score is {score}")
your score is 0
print(f"your score is {score}, your height is [height}, you are winning is{isWinning}")
SyntaxError: f-string: single '}' is not allowed
