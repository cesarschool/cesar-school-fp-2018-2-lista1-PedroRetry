def main():
    d = int(input('por quantos dias você rodou com o carro?')) #d=número de dias
    k = float(input('quantos quilômetros você rodou nesses dias?')) #K=quilômetros rodados o=orçamento
    o1 = 60*d
    o2 = 0.15*k
    of = o1+o2
    print('você terá que pagar R$', of)
if __name__ == '__main__':
    main()
