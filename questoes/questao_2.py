## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
   p = float(input('quantos graus está nesse momento?')) #p=pergunta e f=fórmula
   f = 1.8*p+32
   print('lá fora está', p, 'graus em celsius', 'e', f, 'graus em fahrenheit')
if __name__ == '__main__':
    main()
