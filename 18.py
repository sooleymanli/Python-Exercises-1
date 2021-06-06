#18
# İstifadəçi 0 daxil edənə qədər input daxil etsin daxil etdiklerini toplayın 0 daxil edəndə bitsin və cəm ekrana verilsin.

a=int(input("Ədəd daxil edin: "))
total=0
n=0
while a!=n:
    total=total+a
    a=int(input("Ədəd daxil edin:"))
    if a==n:
        print("Cəm: {}".format(total))
        break