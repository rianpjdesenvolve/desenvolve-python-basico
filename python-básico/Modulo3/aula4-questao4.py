
# Solicitar a distância da entrega em quilômetros
distancia = float(input("Insira a distância da entrega em quilômetros: "))
# Solicitar o peso do pacote em quilogramas
peso = float(input("Insira o peso do pacote em quilogramas: "))

# Calcular o valor do frete com base na distância
if distancia <= 100:
    valor_frete = peso * 1.00
elif 101 <= distancia <= 300:
    valor_frete = peso * 1.50
else:
     valor_frete = peso * 2.00

# Acrescentar uma taxa de R$10 para pacotes com peso superior a 10 kg
if peso > 10:
    valor_frete += 10.00

# Imprime o valor do frete
print(f"O valor do frete é: R${valor_frete:.2f}")
