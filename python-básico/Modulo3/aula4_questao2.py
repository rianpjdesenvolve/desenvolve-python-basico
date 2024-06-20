 # Solicitar ao usuário para inserir a avaliação
avaliacao= int (input(" Avalie o filme (em uma escala de 1 a 5): "))

# Verificar a avaliação e imprime a mensagem correspondente
if avaliacao == 5:
    print("Excelente!")

elif avaliacao == 4:
    print("Muito Bom!")

elif avaliacao == 3:
    print("Bom!")

elif avaliacao == 2:
    print("Regular!")

elif avaliacao == 1:
    print("Ruim!")

else:
    print("Avaliação inválida. Por favor, insira um número entre 1 e 5.")