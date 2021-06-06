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
      