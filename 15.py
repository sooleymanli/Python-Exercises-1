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
      