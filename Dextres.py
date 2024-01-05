
print("Hello world\n")

emp_dic = {}
dup_dic = {}
a = ['fname', 'lname']
b = ['Arjun', 'Govindarajan']
emp_dic['Arjun'] = 1
emp_dic['Arj'] = 2
emp_dic['jun'] = 3
print(emp_dic)
dup_dic = dict(zip(a,b))
print(dup_dic)

print("Python Online Compiler"[::-1])
s="Dextris pvt lmt"
print(s)
print("".join(reversed(s)))

x=[10,20,30,40]
y=[30,40,50,60]

lst = []


for i in x:
    if i in y:
        lst.append(i)
print(lst)
print("arvsdc",[i for i in x if i in y])

dup = [i for i in range(1, 11)]
odd = [i for i in dup if i % 2 != 0]
even = [i for i in dup if i % 2 == 0]
print(odd)
print(even)
print(dup)

class a():
    def __init__(self, name):
        self.name = name

obj = a("Arjun")

print(obj.name)