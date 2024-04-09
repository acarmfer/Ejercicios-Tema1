import sys

def descomponer_numero(numero):
    longitud = len(numero)
    for i, digito in enumerate(numero):
        valor = int(digito)
        descomposicion = valor * 10 ** (longitud - i - 1)
        print(f"{descomposicion:04d}")

def mostrar_instrucciones():
    print("Uso: python descomposicion.py [numero_entero_positivo]")
    print("Ejemplo: python descomposicion.py 3647")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        mostrar_instrucciones()
    else:
        numero = sys.argv[1]
        if not numero.isdigit() or int(numero) <= 0:
            print("Error: Debe ingresar un número entero positivo.")
        else:
            descomponer_numero(numero)
