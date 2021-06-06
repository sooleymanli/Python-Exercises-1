#14          
# İstifadəçinin daxil etdiyi ədədin faktorialını print etdirin.
a=int(input("Ədəd daxil edin: "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
    
print("""
      Daxil etdiyiniz ədəd: {}
      Ədədin factorialı: {}
      """.format(a,factorial))
      