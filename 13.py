#13
# İstifadəcinin daxil etdiyi ədədin təkmi cütmü olduğunu print etdirin. Əgər təkdirsə kvadratını, cütdürsə 5-ə bölünməsindən alınan qalığı print etdirin. 
a=int(input("Ədəd daxil edin: "))
if a==0:
    print("Ədəd 0 -dır və nə sadədir nə mürəkkəb")
else:
    if a%2==0:
        number=a%5
        print("""
          Daxil etdiyiniz ədəd: {}
          Ədəd cüt ədəddir
          Ədədin 5-ə bölünməsindən alınan qalıq: {}""".format(a,number))
    else:
        number_sqr=a*a
        print("""
          Daxil etdiyiniz ədəd: {}
          Ədəd tək ədəddir
          Ədədin kvadratı: {}""".format(a,number_sqr))