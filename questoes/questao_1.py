## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    S = int(input('quanto você ganha?')) #S=Salário
    A = int(input('em quantos porcento seu salário aumentou: ')) #A=Aumento
    P = S*A/100 #P=porcentagem
    R = S+P #R=resultado
    print('seu aumento foi de R$', P, 'e seu novo salário é de R$', R)
if __name__ == '__main__':
     main()
