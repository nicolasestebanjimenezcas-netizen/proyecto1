uv = int(input("Ingrese el índice UV (número entero): "))

if uv <= 2:
    print("Bajo: usa gafas de sol.")
elif uv <= 5:
    print("Moderado: aplica bloqueador FPS 30.")
elif uv <= 7:
    print("Alto: bloqueador FPS 50 y gorra.")
elif uv <= 10:
    print("Muy alto: evita el sol al mediodía.")
else:
    print("Extremo: permanece bajo techo.")