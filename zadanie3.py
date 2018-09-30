cenaSamochodu = int(input ("Podaj cene samochodu: "))

podatek = int(cenaSamochodu*0.14)
print("Podatek wynosi 14% ",podatek)
oplataRejestracyjna = int(cenaSamochodu*0.05)
print("Opłata rejestracyjna wynosi 5% ", oplataRejestracyjna)

prowizja = 150
print("prowizja ", prowizja)
oplataDostarczenie = 500
print("oplata dostarczenia ", oplataDostarczenie)

total = cenaSamochodu+prowizja+oplataDostarczenie+podatek+oplataRejestracyjna
print("Faktyczna cena samochodu wynosi ", total)
