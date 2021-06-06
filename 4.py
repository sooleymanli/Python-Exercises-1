#4        
# Deyək ki, bir string var, məsələn S='Fuadd'. Bunun içində tapın ki, hər hərfdən neçə dənədir(dictionary formatında print edin). {F:1, a:1} və s. şəkildə.
yazi="Fuadd"
thisdict= {}
for i in range(0,len(yazi)):
    herf=yazi[i]
    sayi=int(yazi.count(yazi[i]))
    thisdict["{} hərfinnən".format(herf)] = "{} -ədəd".format(sayi)
print(thisdict)