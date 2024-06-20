    # Coletando informações do personagem
classe_personagem= input("Escolha a classe (Guerreiro, Mago, Arqueiro): ")
forca= int(input(" Digite os pontos de força (de 1 a 20): ")) 
magia= int(input("Digite os pontos de magia (de 1 a 20): "))

# Verificando se o personagem atende aos critérios
atende_criterios = (
        (classe_personagem == "Guerreiro" and forca >= 15 and magia <= 10) or
        (classe_personagem == "Mago" and forca <= 10 and magia >= 15) or
        (classe_personagem == "Arqueiro" and 5 < forca <= 15 and 5 < magia <= 15)
    
    
)
#saída
print(f"Pontos de atributo consistentes com a classe escolhida: {atende_criterios}")