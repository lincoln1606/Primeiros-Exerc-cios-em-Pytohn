velocidade = float(input("Digite a velocidade média (km/h): "))
tempo = float(input("Digite o tempo gasto na viagem (horas): "))

distancia = tempo * velocidade

litros_usados = distancia / 12

print("\nResultados:")
print(f"Velocidade média: {velocidade} km/h")
print(f"Tempo gasto: {tempo} horas")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {litros_usados:.2f} litros")
