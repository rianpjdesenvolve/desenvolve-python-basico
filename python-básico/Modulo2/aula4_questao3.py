# Entrada de dados pelo usuário
produto1= input("Digte o nome do primeiro produto: ")
preco_produto1= float (input("Informe o valor do primeiro produto: "))
quantidade_produto1= int (input("Informe a quantidaade comprada do primeiro produto: "))

produto2= input("Digte o nome do segundo produto: ")
preco_produto2= float (input("Informe o valor do segundo produto: "))
quantidade_produto2= int (input("Informe a quantidade comprada do segundo produto: "))

produto3= input("Digte o nome do terceiro produto: ")
preco_produto3= float (input("Informe o valor do terceiro produto: "))
quantidade_produto3= int (input("Informe a quantidade comprada do terceiro produto: "))

#processamento
valor_compra= (preco_produto1 * quantidade_produto1) + (preco_produto2 * quantidade_produto2) + (preco_produto3 * quantidade_produto3)

#saida

print(f"Total: R$ {valor_compra:,.2f}")