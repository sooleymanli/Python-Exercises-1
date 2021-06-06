#8
# İstifadəçinin daxil etdiyi ədədin sadə yoxsa mürəkkəb olduğunu print etdirin.
n = int(input("Ədəd daxil edin:"))
novu=""
if n < 2:
    print("Ədəd 1-dən böyük olmalıdır!")
elif n == 2:
    print("Sadə ədəddir")
else:
    for i in range(2, n):
        if n % i == 0:
           novu="Mürəkkəb ədəddir"
           break
        elif i*i == n:
            novu="Mürəkkəb ədəddir"
            break
        else:
           novu ="Sadə ədəddir"
print(novu)