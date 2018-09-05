def main():
    from math import pi
    r = float(input('quer saber a medidas do seu circulo,então de me diga o raio:'))
    a = pi*r**2
    d = r*2
    c = 2*pi*r
    print('parabéns você descobrio a área:', a, 'o diâmetro:', d, 'e o compremento:', c, 'do seu circulo')
if __name__ == '__main__':
    main()
