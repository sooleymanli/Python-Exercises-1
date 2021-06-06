#6    
# İstifadəçidən bir ədəd alın ve 1-dən bu ədədə qədər olan tək ədədləri bir,cüt ədədləri də bir toplayin. Sonda hər iki nəticənin print etdirin.Print edərkən format() metodundan istifadə edin. 
eded = int(input("Ədəd daxil edin:"))
tekeded= 0
cuteded=0
for i in range(eded):
    if i%2==0:
        cuteded=cuteded+i
    else:
        tekeded=tekeded+i
print("""
      Daxil etdiyiniz ədəd: {}
      Tək ədədlərin cəmi: {} 
      Cüt ədədlərin cəmi: {}""".format(eded,tekeded,cuteded))