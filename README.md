# python_labs

# Лабораторная работа №1

## задание 1
```python
name = str(input("Имя: "))
age = int(input("Возраст: "))
print("Привет, ", name, "! Через год тебе будет ", age+1, ".",sep = '')
```

![](./images/lab01/ex01.png)

## задание 2
```python
a = float(input("a:"))
b = float(input("b:"))
sum = a+b
print("sum=", sum , "avg=", sum/2)
```

![](./images/lab01/ex02.png)

## задание 3
```python
price = float(input())
discount = float(input())
vat = float(input())
base =  price * (1 - discount/100)
print("База после скидки:  ", base, "₽")
print("НДС:                ", base * (vat/100), "₽")
print("Итого к оплате:     ", base+ base * (vat/100), "₽")
```

![](./images/lab01/ex03.png)

## задание 4
```python
m = int(input("Минуты: "))
h = m // 60
min = m % 60
print(f"{h}:{min:02d}")
```

![](./images/lab01/ex04.png)

## задание 5
```python
fio = str(input("ФИО:"))
FIO = fio.title().split()
surname = FIO[0]; name = FIO[1]; fname = FIO[2]
length = len(surname) + len(name) + len(fname) + 2
print("Инициалы: ", surname[0], name[0], fname[0], sep = '')
print("Длина (символов):", length)
```

![](./images/lab01/ex05.png)

## задание 6
```python
N = int(input("Число строк:"))
o = 0; z = 0
for i in range(N):
    member = str(input()).split()
    q = member[3]
    if q == "True":
        o = o + 1
    if q == "False": 
        z = z + 1
print(o,z)
```

![](./images/lab01/ex06.png)

## задание 6
```python
sh = input()

start = -1
for i, ch in enumerate(sh):
    if ch.isupper():
        start = i
        break

second = start
for i in range(len(sh) - 1):
    if sh[i].isdigit() and sh[i+1].isalpha():
        second = i + 1
        break

step = second - start

result = []
i = start
while i < len(sh):
    result.append(sh[i])
    i += step

result = ''.join(result)
print(result)
```

![](./images/lab01/ex07.png)




# Лабораторная работа 2
## задание 1

## задание 3
![alt text](image.png)
