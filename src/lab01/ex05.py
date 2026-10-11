fio = str(input("ФИО:"))
FIO = fio.title().split()
surname = FIO[0]
name = FIO[1]
fname = FIO[2]
length = len(surname) + len(name) + len(fname) + 2
print("Инициалы: ", surname[0], name[0], fname[0], sep="")
print("Длина (символов):", length)
