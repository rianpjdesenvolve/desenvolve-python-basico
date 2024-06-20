# Coletando informações do usuário
genero= input("Informe seu gênero (M ou F): ")
idade= int (input("Informe sua idade: "))
tempo_servico= int(input("Informe o tempo trabalhado (em anos): "))

#processamento
a = (genero== "F" and idade > 60) or \
    (genero== "M" and idade > 65)
b= tempo_servico >= 30
c= idade== 60 and tempo_servico >= 25

pode_aposentar= a or b or c

print(pode_aposentar)