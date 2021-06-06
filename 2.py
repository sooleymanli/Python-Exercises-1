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