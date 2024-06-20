#entrada de dados do ususário
idade_juliana= int(input("Informe a idade de Juliana: "))
idade_cris= int(input("Informe a idade de Cris: "))

#processamento
pode_entrar= idade_juliana > 17 and idade_cris > 17

#saída
print(pode_entrar)