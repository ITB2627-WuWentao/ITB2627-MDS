edat = int(input("Quina edat tens? "))

if edat <= 0:
    print("Impossible")
elif edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")

print("Programa Finalitzat")