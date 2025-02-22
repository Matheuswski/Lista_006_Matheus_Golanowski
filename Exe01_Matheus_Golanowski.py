#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
print("Matheus Golanowski")
pais = ("Brasil", "Alemanha", "Colombia", "Egito", "Israel")
print(pais)
escolha = input("escolha um país: ")
if escolha in pais:
    indi = pais.index(escolha)
    print("O indice do pais é :", indi)
else:
    print("país invalido!")

    
