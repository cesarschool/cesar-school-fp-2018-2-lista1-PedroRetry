def main():
    c = int(input('quantos cigarros você fuma por dia'))
    a = int(input('por quantos anos você vem fumando')) #c=cigarros a=anos a1=1 ano tem 365 dias,quantidade de anos em dias 
    a1 = a*365
    c1 = c*a1
    d = c1/144
    print('você perderá', d, 'dias de vida')
if __name__ == '__main__':
    main()
