#7      
# İstifadəçidən bir string alın və içərisindəki rəqəmləri print etdirin.
yazi=input("Söz daxil edin:")
yeni_yazi=""
for i in range(0,len(yazi)):
    if yazi[i].isnumeric()==True:
        yeni_yazi=yeni_yazi+" "+yazi[i]
print("Daxil etdiyiniz sözün daxilindəki rəqəmlər: "+yeni_yazi)     