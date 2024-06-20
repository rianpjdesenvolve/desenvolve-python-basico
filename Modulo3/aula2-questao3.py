
    # Coletando informações do usuário
idade = int(input("Digite sua idade: "))
numero_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
vitorias = int(input("Quantos jogos já venceu? "))

    # Verificando se o usuário atende aos critérios para ingressar no clube
apto = (16 <= idade <= 18) and numero_jogos and (vitorias >= 1)

    # Imprimindo o resultado
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")
