# Entrada de dados do usuário
comprimento= int (input("Digite o comprimento do terreno:"))
largura= int(input("Digite a largura do terreno:"))
preco_m2= float(input("Digte o valor do m²:"))

#processamneto do dados
area_m2= comprimento * largura
preco_terreno= area_m2 * preco_m2

# saída dos dados
print(f"O terreno possui {area_m2}m2 e custa R${preco_terreno: ,.2f}")