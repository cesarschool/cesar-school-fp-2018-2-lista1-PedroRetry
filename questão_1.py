def main():
    S = int(input('quanto você ganha?')) #S=Salário
    A = int(input('em quantos porcento seu salário aumentou: ')) #A=Aumento
    P = S*A/100 #P=porcentagem
    R = S+P #R=resultado
    print('seu aumento foi de R$', P, 'e seu novo salário é de R$', R)
if __name__ == '__main__':
    main()
