# TODO Найдите количество книг, которое можно разместить на дискете

book  = 100*50*25*4
kol = 1024 * 1.44 * 1024

itog = kol//book

print("Количество книг, помещающихся на дискету:", int(itog))