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