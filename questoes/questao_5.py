## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    c = int(input('quantos cigarros você fuma por dia'))
    a = int(input('por quantos anos você vem fumando')) #c=cigarros a=anos a1=1 ano tem 365 dias,quantidade de anos em dias 
    a1 = a*365
    c1 = c*a1
    d = c1/144
    print('você perderá', d, 'dias de vida')
if __name__ == '__main__':
    main()
