import os
import sys


# a = "life is too short, you need python"
# print(a)
# print(a[0:4])
# print(a[5:7], a[12:17])

# b = "20191906YujinPark"
# id = b[0:8]
# name = b[8:17]

# print("id : ",id)
# print("name : ",name)

# c = "20191906" + "YujinPark"
# print("c : ",c)

# print("--------------------------------")
# print("I eat %d apples." % 3)
# print("I eat %s apples." % "five")
# print("I get %d, but I eat %s apples." % (15, "five"))

# print("%10s bye" % "hi")
# print("%-10s bye" % "hi")

# print("I get {0}, but I eat {1} apples.".format(15, "five"))
# print("%0.4f" % 3.42134234234)

# print("I ate {number} apples. so I was sick for {day} days".format(number=10, day=3))
# print("I ate {0} apples. so I was sick for {day} days".format(10, day = 3))
# print("{0:<10}".format("hi"))
# print("{0:>10}".format("hi"))
# print("{0:^10}".format("hi"))

# print("{0:=<10}".format("hi"))
# print("{0:!>10}".format("hi"))
# print("{0:0.4f}".format(3.42134234234))

# print("{{ and }}".format())

# name = "Yujin Park"
# age = 26

# print(f"이름: {name}, 나이: {age}")
# print(f"내년 이면  {age + 1} 살.")

# d = {'name': 'Yujin Park', 'age': 26}
# print(f'이름: {d["name"]}, 나이: {d["age"]}')

# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')


# print("="*50)
# a = "hobby"
# print(a.count('b'))
# print("/".join(a))

# print(a.find('b'))
# print(a.find('x'))

# print(a.index('b'))
# print(a.index('x'))



# a = "     hi      "
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

# print(a.split())



# print("="*50)

# dic = {'name': 'Yujin Park', 'age': 26, 'phone': '010-1234-5678', 'birth': '0620'}
# a = {1 : 'hi'}
# print(a)

# a2 = {'a': [1,2,3]}
# print(a2)

# a[2] = 'b'
# print(a)

# a['name'] = 'Yujin Park'
# print(a)

# a[3] = [1,2,3]
# print(a)

# del a[1]
# print(a)

# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])
# print(grade['julliet'])

# a = {1:'a', 1:'b'}
# print(a)
# # a = {[1, 2]: 'hi'}
# # print(a)

# a = {'name': 'Yujin Park', 'phone': '010-1234-5678', 'birth': '0620'}
# print(a.keys())
# print(list(a.keys()))

# print(a.values())
# print(list(a.values()))

# print(a.items())
# print(list(a.items()))

# a.clear()
# print(a)

# print('name' in a)
# print('email' in a)

# a = {'name': 'Yujin Park', 'phone': '010-1234-5678', 'birth': '0620'}
# print(a.get('name'))
# print(a.get('phone'))
# print(a.get('birth'))

# # print(a.get('email'))
# print(a.get('email', 'foo'))


print("="*50)

s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

s1  = set([1,2,3, 4, 5, 6])
s2 = set([4,5,6,7,8])

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

s1.add(40)
print(s1)

s1.update([7,8,9])
print(s1)

s1.remove(40)
print(s1)

a = True
b = False
print(type(a))
print(type(b))

print(1 == 1)
print(1 > 2)
print(1 < 2)

print(bool('python'))
print(bool(''))

print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))


a = 1
b = "python"
c = [1,2,3]

print(id(a))
b = a
print(id(b))

print(a is b)
a = [1,2,3]
a[1] = 4
print(a)
print(b)

print(a[:])


from copy import copy
a = [1,2,3]
b = copy(a)
print(a)
print(b)
print(a is b)



a,b = ('python', 'life')
a, b = 'python', 'life'

[a,b] = ['python', 'life']
a = b = 'python'

a = 3
b  =5

a, b = b, a
print(a)
print(b)







>>>>>>> 70e6f91fc079ce6262c723bcf9c2795d19b79d88
