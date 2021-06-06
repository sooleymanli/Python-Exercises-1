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