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
