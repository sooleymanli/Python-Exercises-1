#1
# İstifadəçidən çevrənin radiusunu alın və uzunluğunu hesablayın. 
r = int(input("Çevrənin radiusunu daxil edin:"))
l = r*2*3.14
print("Çevrənin uzunluğu: "+" "+ str(l))


#2
# Tutaq k, n=13 istifadəçi 13 daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə tapdığını print etsin.
cehd = 1
n = 13
a = int(input("Ədəd daxil edin:"))
while a != n:
    cehd = cehd + 1
    a = int(input("Ədəd daxil edin:"))
    if a == n:
        print("Düzgündür " + str(cehd) + " dəfə")
        break
    
    
#3
# 5-ə bölünən və 30-dan kiçik ədədləri print etdirin.
i=0
while i < 29:
    i=i+1
    if i%5 == 0:
        print(i)
        
        
#4        
# Deyək ki, bir string var, məsələn S='Fuadd'. Bunun içində tapın ki, hər hərfdən neçə dənədir(dictionary formatında print edin). {F:1, a:1} və s. şəkildə.
yazi="Fuadd"
thisdict= {}
for i in range(0,len(yazi)):
    herf=yazi[i]
    sayi=int(yazi.count(yazi[i]))
    thisdict["{} hərfinnən".format(herf)] = "{} -ədəd".format(sayi)
print(thisdict)





#5
# İstifadəcinin daxil etdiyi ədədin təkmi cütmü olduğunu print etdirin.
input6=int(input("Ədəd daxil edin:"))
if input6%2==0:
    print("Cüt ədəddir")
else:
    print("Tək ədəddir")





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






#7      
# İstifadəçidən bir string alın və içərisindəki rəqəmləri print etdirin.
yazi=input("Söz daxil edin:")
yeni_yazi=""
for i in range(0,len(yazi)):
    if yazi[i].isnumeric()==True:
        yeni_yazi=yeni_yazi+" "+yazi[i]
print("Daxil etdiyiniz sözün daxilindəki rəqəmlər: "+yeni_yazi)     





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






#9
# İstifadəçidən 2 ədəd alin ve bu iki ədəd arasindaki sadə ədədlərin ortalamasını print etdirin.
a = int(input("Birinci ədədi daxil edin: "))
b = int(input("İkinci ədədi daxil edin: "))

if a>b:
    new_range = range(b+1,a)
else:
    new_range = range(a+1,b)

simple_number_total=0
number_times=0
simple_number_total_string=""
for i in new_range: 
    if i==2:
        simple_number_total_string=simple_number_total_string+str(2)
        simple_number_total=simple_number_total+2
        number_times=number_times+1
    else:
        for j in range(2,i):
            if i%j==0:
                number_type=False 
                number=0
                break
                
            elif j*j==i:
               number_type=False 
               number=0
               break
            else:
                number_type=True
                number=i
                
        if number_type==True:
            number_times=number_times+1
        simple_number_total=simple_number_total+number
        if number!=0:
            simple_number_total_string =simple_number_total_string +" "+ str(number)

number_average=simple_number_total/number_times 
    
print("""
      Daxil etdiyiniz ədədlər: {} və {}
      Sadə ədədlər: {}
      Ədədlərin cəmi: {}
      Ədədlərin ədədi ortası:{}
      """.format(a,b,simple_number_total_string,simple_number_total,number_average))
      
 
      

#10
# Daxil edilmiş string-in tərsini print etdirin (hazır metod isitfadə etmədən).
new_str = input("Söz daxil edin:")
new_word=""
for i in range(len(new_str)-1,-1,-1):
    new_word=new_word+new_str[i]
    
print(new_word)    






#11
# İstifadəçi 2 ədəd daxil etsin və bu 2 ədəd arasındaki sadə ədədlərin cəmini tapın.
a = int(input("Birinci ədədi daxil edin: "))
b = int(input("İkinci ədədi daxil edin: "))
if a>b:
    new_range = range(b+1,a)
else:
    new_range = range(a+1,b)
simple_number_total=0
number_times=0
simple_number_total_string=""
for i in new_range:    
    if i==2:
        simple_number_total_string=simple_number_total_string+str(2)
        simple_number_total=simple_number_total+2
    else:
        for j in range(2,i):
            if i%j==0:
                number_type=False 
                number=0
                break
                
            elif j*j==i:
               number_type=False 
               number=0
               break
            else:
                number_type=True
                number=i
                
        if number_type==True:
            number_times=number_times+1
        simple_number_total=simple_number_total+number
        if number!=0:
            simple_number_total_string =simple_number_total_string +" "+ str(number)
          
print("""
      Daxil etdiyiniz ədədlər: {} və {}
      Sadə ədədlər: {}
      Ədədlərin cəmi: {}
      """.format(a,b,simple_number_total_string,simple_number_total,))   
      
      
      


#12      
# s=” AXC, Parlament, Gəncə, May,” verilmiş stringdə sonuncu  vergülün index-ni print etdirin.
s="AXC, Parlament, Gəncə, May,"
print(len(s)-1)





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
      
      


#15      
# İstifadəçidən 2 ədəd alın və yerlərini dəyişin
a = int(input("Birinci Ədədi daxil edin: "))
b = int(input("İkinci Ədədi daxil edin: "))
print("""
      Birinci ədəd: {}
      Ikinci ədəd: {}""".format(a,b))
a,b=b,a
print(""" Yerləri dəyişildikdən sonra:
      Birinci ədəd: {} 
      Ikinci ədəd: {}""".format(a,b))  
      
      
      
      
      
 
      
#16
# 1-dən istifadəçinin daxil etdiyi ədədə qədər olan sadə ədədləri bir,mürəkkəb ədədləri bir toplayın və format istifadə edərək print etdirin.
a = int(input("Ədəd daxil edin: "))
simple_number_total=0
simple_number_total_string=""
complex_number_total=0
complex_number_total_string=""
new_range =range(1,a)
complex_number=0
simple_number=0
for i in new_range:    
    if i==2:
        simple_number_total_string=simple_number_total_string+str(2)
        simple_number_total=simple_number_total+2
    else:
        for j in range(2,i):
            if i%j==0:
                simple_number=0
                complex_number=i
                break
                
            elif j*j==i:
                simple_number=0
                complex_number=i
                break
            else:
                simple_number=i
                complex_number=0
            
        complex_number_total=complex_number_total+complex_number
        simple_number_total=simple_number_total+simple_number
        
        if simple_number!=0:
            simple_number_total_string =simple_number_total_string +" "+ str(simple_number)
        if complex_number!=0:
            complex_number_total_string=complex_number_total_string+" "+str(complex_number)
print("""
      Daxil etdiyin rəqəm: {}
      Sadə ədədlər: {}
      Sadə Ədədlərin cəmi: {}
      Mürəkkəb ədədlər: {}
      Mürəkkəb ədədlərin cəmi {}
      """.format(a,simple_number_total_string,simple_number_total,complex_number_total_string,complex_number_total))
      
      
      
      


#17      
# 0-dan 100-ə qədər cüt ədədləri toplayın, amma bunu while ilə edin.
i=0
cem=0
while i<100:
    i=i+1
    if i%2 == 0:
     cem=cem+i
print(cem)    





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
          




#19  
# Bir list götürün və listdəki ən böyük və ən kiçik ədədi ekrana yazdırın.

list = [5,7,9,12,85,76,4]

a = list[len(list)-1]
for i in list:
    if i < a:
        a = i
        
b = list[0]
for j in list:
    if j>b:
        b=j

print("""
      Listimiz: {}
      Ən kiçik: {}
      Ən böyük: {}
      """.format(list,a,b))   
    





#20    
# İstifadəçidən adını alın məsələn "Süleymanlı" bunun hərflərini print etdirin amma çalışın while ilə edin

new_name=input("Ad daxil edin: ")
a=0
while a<len(new_name):
    print(new_name[a])
    a=a+1
    if a==len(new_name):
        break