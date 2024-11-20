cadena = input("Introdueix una cadena: ")
vocals = "aeiouAEIOU"
comptador = 0

for lletra in cadena:
    if lletra in vocals:
        comptador += 1

print(f"El nombre de vocals en la cadena és: {comptador}")
