## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    d = int(input('por quantos dias você rodou com o carro?')) #d=número de dias
    k = float(input('quantos quilômetros você rodou nesses dias?')) #K=quilômetros rodados o=orçamento
    o1 = 60*d
    o2 = 0.15*k
    of = o1+o2
    print('você terá que pagar R$', of)
if __name__ == '__main__':
    main()
