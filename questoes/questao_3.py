## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import pi
def main():
    r = float(input('quer saber a medidas do seu circulo,então de me diga o raio:'))
    a = pi*r**2
    d = r*2
    c = 2*pi*r
    print('parabéns você descobrio a área:', a, 'o diâmetro:', d, 'e o compremento:', c, 'do seu circulo')
if __name__ == '__main__':
    main()
