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