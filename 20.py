#20    
# İstifadəçidən adını alın məsələn "Süleymanlı" bunun hərflərini print etdirin amma çalışın while ilə edin

new_name=input("Ad daxil edin: ")
a=0
while a<len(new_name):
    print(new_name[a])
    a=a+1
    if a==len(new_name):
        break