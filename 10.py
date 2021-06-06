#10
# Daxil edilmiş string-in tərsini print etdirin (hazır metod isitfadə etmədən).
new_str = input("Söz daxil edin:")
new_word=""
for i in range(len(new_str)-1,-1,-1):
    new_word=new_word+new_str[i]
    
print(new_word)    