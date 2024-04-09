texto1 = "Hola Mundo"
texto2 = "Hola Mundo"
texto3 = "Hola Mundo"
numero1 = 150
numero2 = 7887
numero3 = 20.02

resultado1 = "{:>20}".format(texto1)
resultado2 = "{:.3}".format(texto2)
resultado3 = "{:^20.1}".format(texto3)
resultado4 = "{:05d}".format(numero1)
resultado5 = "{:7d}".format(numero2)
resultado6 = "{:03.3f}".format(numero3)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)